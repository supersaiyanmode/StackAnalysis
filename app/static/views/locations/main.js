function loadLocations(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/locations/"
	}).done(successFn).fail(errorFn);
}

function locationsInit() {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadLocations(function(data) {
		loadTable(divSelector, data);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

$(locationsInit);
