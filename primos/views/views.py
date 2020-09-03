from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from ..models.result import Result


@require_http_methods(["GET"])
def home(request):
    """ Main view - Homepage """
    return render(request, 'home.html')
