$(function()
    {
        var name;
        $('#name').bind('input', function() { 
                name = $(this).val();
                getData(name);
        });
        
    });

function getData(name) {
    if (name !== undefined) {
            $.get("/salary", {name: name }, function(data) {
                    showData(data);
                })
        }
    } 

function showData(data) {
    $("#result").remove();
    $(".container").append(data);
}
