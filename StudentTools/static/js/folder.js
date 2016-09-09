var csrftoken = Cookies.get('csrftoken');

$("#btn").mouseup(function(){
    $(this).blur();
})
$("button").mouseup(function(){
    $(this).blur();
})
$(document).ready(function()
{
    $("button").click(function()
    {
    	var thisId = $(this).attr("id");
    	
        // If button's id is remove, remove the course from folder
    	if ( thisId == 'remove') {
    	var cid ;
 		cid = $(this).attr("this-course-id");
 		var $this = $(this);
        $.ajax(
        {
        	url: "/degreeplan/removeFromFolder/", 
        	method: "POST",
        	data: 
        	{ csrfmiddlewaretoken: csrftoken,course_id: cid},
        	success: function(data,status)
        	{
        		alert(data + "is removed from your folder\nStatus: " + status);
        		$this.closest('tr').remove();

        	},
    	});    
    	}

        // If button's id is remove, remove the course from folder
        if ( thisId == 'addToPlanner') {
        var cid , formData;
        cid = $(this).attr("this-course-id");
        formData = $("#dropdown-sem option:selected").text();
        s1 = cid+"addToPlannerModal";
        s2 = cid + "addToPlannerSpan";
        s3 = cid +"glyphiconAddToPlanner";
        $addToPlannerModal = $(s1);
        $addToPlannerSpan = $(s2);
        $glyphiconAddToPlanner = $(s3);
        $.ajax(
        {
            url: "/degreeplan/addToPlanner/", 
            method: "POST",
            data: 
            { csrfmiddlewaretoken: csrftoken,course_id: cid, sem_year: formData},
            success: function(data,status)
            {

                alert(data + "is added to your Planner\nStatus: " + status);
                $addToPlannerSpan.attr({
                    "title" : "Added in Planner"
                });
                $glyphiconAddToPlanner.attr({
                    "class": "glyphicon glyphicon-ok"
                })

            },
        });
        }    

    });
});