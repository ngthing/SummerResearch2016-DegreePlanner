var csrftoken = Cookies.get('csrftoken');

$(document).ready(function()
{
    $("button").click(function()
    {
    	var cid ;
 		cid = $(this).attr("this-course-id");
 		var str = "#" + cid + "addToFolder";
 		var $addSign = $(str);
        $.ajax(
        {
        	url: "/degreeplan/addToFolder/", 
        	method: "POST",
        	data: 
        	{ csrfmiddlewaretoken: csrftoken,courseid : cid},
        	success: function(data,status)
        	{
        		alert(data + "is added to your folder\nStatus: " + status);
        		$addSign.text( "In Folder" );

        	},
            error: function()
            {
                alert("Please Log in or Sign up to add this course to folder");

            }
    	});    
    });
});
$("button").mouseup(function(){
    $(this).blur();
})