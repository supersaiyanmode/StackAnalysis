function loadLocations(page, successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/locations/?page=" +page
	}).done(successFn).fail(errorFn);
}

function loadTablePage(num) {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadLocations(num, function(data) {
		loadTable(divSelector, data);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

function loadPage(event, num) {
	loadTablePage(num);
}

function locationsInit() {
	loadTablePage(0);
	
	var params = {total: 10}
	loadPagination('#page-selection', params, loadPage);
}

$(locationsInit);
