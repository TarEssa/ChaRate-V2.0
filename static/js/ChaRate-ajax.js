
$('#suggestion').keyup(function(){ 
    var query;
    query = $(this).val();
    $.get('/ChaRate/suggest/', {suggestion: query}, function(data){
            $('#chars').html(data);
        });
    });

$('#likes').click(function(){ var charid;
    charid = $(this).attr("data-charid");
    $.get('/ChaRate/like/', {character_id: charid}, function(data){
            $('#like_count').html(data);
                $('#likes').hide();
    }); 
})