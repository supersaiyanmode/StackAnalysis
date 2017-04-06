function loadAnswers(page, successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/answers/?page="+page
	}).done(successFn).fail(errorFn);
}

function loadTablePage(num) {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadAnswers(num, function(data) {
		loadTable(divSelector, data);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}


function loadPage(event, num) {
	loadTablePage(num);
}

function answersInit() {
	loadTablePage(0);
	
	var params = {total: 10}
	loadPagination('#page-selection', params, loadPage);
}

$(answersInit);
