// Global data
let PageURL = $(location).attr("href");
let url_var = PageURL.split('/');
let url_base = url_var[0] + '//' + url_var[1] + url_var[2];

// All info_gen are hide
$('.info_gen').hide();


//  Get regular primes without to save - Button CONSULTAR
$('#btn_cant_reg_not').click(function () {
    $("#info_gen0").show();
    let cant_reg_not = $("#cant_reg_not").val();

    if (cant_reg_not > 1000) {
        alert('Esta solicitud puede tardar un poco.');
    }

    if (cant_reg_not != "") {
        $.ajax({
            url: url_base + '/regular_primes/' + cant_reg_not,
            type: 'GET',
            success: function (result) {
                $("#regular_primes_result").val(result.success);
                $("#info_gen0").hide();
            },
            error: function (myerror) {
                console.log(myerror);
            }
        });
    }

});


//  Get regular primes without to save - Button CONSULTAR
$('#btn_cant_twin_not').click(function () {
    $("#info_gen1").show();
    let cant_twin_not = $("#cant_twin_not").val();
    if (cant_twin_not > 1000) {
        alert('Esta solicitud puede tomar varios minutos.');
    }
    if (cant_twin_not != "") {
        $.ajax({
            url: url_base + '/twin_primes/' + cant_twin_not,
            type: 'GET',
            success: function (result) {
                $("#twin_primes_result").val(result.success);
                $("#info_gen1").hide();
            },
            error: function (myerror) {
                console.log(myerror);
            }
        });
    }

});


//  Get regular primes to save data - Button CONSULTAR
$('#btn_cant_reg_yes').click(function () {
    let cant_reg_yes = $("#cant_reg_yes").val();

    if (cant_reg_yes > 1000) {
        alert('Esta solicitud puede tardar un poco si no se ha realizado antes.');
    }

    if (cant_reg_yes > 2000) {
        alert('Error: Esta solicitud excede los 2000 números.');
    }

    if (cant_reg_yes != "" && cant_reg_yes <= 2000) {
        $("#info_gen2").show();
        $.ajax({
            url: url_base + '/regular_primes_save/' + cant_reg_yes,
            type: 'GET',
            success: function (result) {
                $("#regular_primes_result_save").val(result.success);
                $("#info_gen2").hide();
            },
            error: function (myerror) {
                console.log(myerror);
            }
        });
    }

});


//  Get twins primes to save data - Button CONSULTAR
$('#btn_cant_twin_yes').click(function () {
    let cant_twin_yes = $("#cant_twin_yes").val();

    if (cant_twin_yes > 1000) {
        alert('Esta solicitud puede tomar varios minutos si no se ha realizado antes.');
    }

    if (cant_twin_yes > 2000) {
        alert('Error: Esta solicitud excede los 2000 pares');
    }

    if (cant_twin_yes != "" && cant_twin_yes <= 2000) {
        $("#info_gen3").show();
        $.ajax({
            url: url_base + '/twin_primes_save/' + cant_twin_yes,
            type: 'GET',
            success: function (result) {
                $("#twin_primes_result_save").val(result.success);
                $("#info_gen3").hide();
            },
            error: function (myerror) {
                console.log(myerror);
            }
        });
    }

});