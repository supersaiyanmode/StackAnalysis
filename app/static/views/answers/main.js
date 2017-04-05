function loadAnswers(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/answers/"
	}).done(successFn).fail(errorFn);
}

function answersInit() {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadAnswers(function(data) {
		loadTable(divSelector, data);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

$(answersInit);
