// Load after document is ready

$(document).ready(function () {

    // Hide Preloader
    $("#overlayer").hide();

    // Hide the button after loading the data
    $('#btn-loader').hide();
});

// Button Loader for apply job
$("form").submit(function () {
    $('#submit').hide();
    $('#btn-loader').show();
    $('#btn-loader').attr('disabled', 'disabled');
});

