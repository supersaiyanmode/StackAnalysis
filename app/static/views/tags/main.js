function loadTags(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/tags/"
	}).done(successFn).fail(errorFn);
}

function tagsInit() {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadTags(function(data) {
		loadTable(divSelector, data);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

$(tagsInit);
