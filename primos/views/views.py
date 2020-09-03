from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from ..models.result import Result
from ..models.functions import list_regular_primes, list_twins_primes


@require_http_methods(["GET"])
def home(request):
    """ Main view - Homepage """
    return render(request, 'home.html')


@require_http_methods(["GET"])
def regular_primes(request, quantity):
    """ Return a list with regular prime numbers """
    list_primes = list_regular_primes(quantity)
    return JsonResponse({"success": list_primes})


@require_http_methods(["GET"])
def twin_primes(request, quantity):
    """ Return a list with pairs of twin prime numbers """
    list_pair = list_twins_primes(quantity)
    return JsonResponse({"success": str(list_pair)[1:-1]})


@require_http_methods(["GET"])
def regular_primes_save(request, quantity):
    """  Return a list with regular prime numbers and save them in databse """
    # validate if range exists
    # get object with required quantity
    try:
        obj = Result.objects.get(type='regular', range=quantity)
        return JsonResponse({"success": str(obj.result)[1:-1]})
    except Exception:
        obj = None

    # verify if a bigger range exists, then get the result of that object to select the required quantity for new object
    # to avoid the calculation again
    try:
        greater_than = Result.objects.filter(
            range__gt=quantity, type='regular').order_by("range")[0]
        obj_result = str(json.dump(greater_than.result)[0:quantity])[1:-1]
    except Exception:
        obj_result = str(list_regular_primes(quantity))
    # create object to save data with new range (quantity)
    obj = Result(type='regular', range=quantity)
    obj.result = obj_result
    obj.save()
    return JsonResponse({"success": str(obj.result)[1:-1]})


@ require_http_methods(["GET"])
def twin_primes_save(request, quantity):
    """  Return a list with regular prime numbers and save them in databse """
    # validate if range exists
    # get object with required quantity
    try:
        obj = Result.objects.get(type='twin', range=quantity)
        return JsonResponse({"success": str(obj.result)[1:-1]})
    except Exception:
        obj = None

    # verify if a bigger range exists, then get the result of that object to select the required quantity for new object
    # to avoid the calculation again
    try:
        greater_than = Result.objects.filter(
            range__gt=quantity, type='twin').order_by("range")[0]
        obj_result = str(json.dump(greater_than.result)[0:quantity])[1:-1]
    except Exception:
        obj_result = str(list_twins_primes(quantity))

    obj = Result(type='twin', range=quantity)
    obj.result = obj_result
    obj.save()
    return JsonResponse({"success": str(obj.result)[1:-1]})
