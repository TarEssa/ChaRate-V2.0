
$('#suggestion').keyup(function(){ 
    var query;
    query = $(this).val();
    $.get('/ChaRate/suggest/', {suggestion: query}, function(data){
            $('#chars').html(data);
        });
    });