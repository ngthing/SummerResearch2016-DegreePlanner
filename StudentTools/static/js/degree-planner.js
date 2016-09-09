$(document).ready(function(){
    $('[data-toggle="popover"]').popover();
});	

var showSemYear = function() {
	var $this = $(this);
	var this_semester_year = $(this).attr("value");
	var id_this_semester_year = '#' +this_semester_year;
	
	if ($this.is(':checked')) {
		$(id_this_semester_year).css({"border": "2px solid blue",
	    "border-radius": "8px"});
	}
	else {
		$(id_this_semester_year).css({"border": "0px",
	    "border-radius": "0px"});
	}

};
showSemYear();
 
$( "input[type=checkbox]" ).on( "click", showSemYear );

