function loadUsers(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/questions/"
	}).done(successFn).fail(errorFn);
}

function questionsInit() {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadQuestions(function(data) {
		loadTable(divSelector, data);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

$(questionsInit);
