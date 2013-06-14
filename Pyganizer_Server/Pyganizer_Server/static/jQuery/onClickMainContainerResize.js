var showCalendar;
var showToDoBoard;
var isCalendar;

/** Consts on calendar and todo_board **/
var widthDivA = "849px";
var heighDivA = "610px";

var widthDivD = "100px";
var heightDivD = "100px";

var opacityLevel = 0.2;

$(document).ready(function() {

	showCalendar = function() {
		if (isCalendar) {
			return true;
		}
		isCalendar = true

		$('#calendar').animate({
			width : widthDivA,
			height : heighDivA,
			top : "0px",
			left : "10px",
			opacity : 1
		}, {
			queue : false,
			duration : 1000
		});
        $('#calendar').children().fadeIn();
        $("#new_event").css("display", "none");
		$('#todo_board').animate({
			width : widthDivD,
			height : heightDivD,
			top : "300px",
			left : "1190px",
			opacity : opacityLevel
		}, {
			queuue : false,
			duration : 1000
		});

	}
	
	showToDoBoard = function() {

		if (!isCalendar) {
			return true;
		}
		isCalendar = false;
		$('#todo_board').animate({
			width : widthDivA,
			height : heighDivA,
			top : "0px",
			left : "190px",
			opacity : 1
		}, {
			queue : false,
			duration : 1000
		});
        $('#todo_board').children().fadeIn();
        $('#calendar').children().fadeOut();
        $('#calendar').animate({
			width : widthDivD,
			height : heightDivD,
			top : "300px",
			left : "10px",
			opacity : opacityLevel
		}, {
			queuue : false,
			duration : 1000
		});

	}

	$('#calendar').click(showCalendar);

	$('#todo_board').click(showToDoBoard);
	showCalendar();
});

