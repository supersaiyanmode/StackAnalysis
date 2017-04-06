function loadUsers(page, successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/users/?page=" +page
	}).done(successFn).fail(errorFn);
}

function loadTablePage(num) {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadUsers(num, function(data) {
		loadTable(divSelector, data);
		var params = {
			total: Math.ceil(data.meta.rows / data.meta.page_size),
			maxVisible: 10
		};
		loadPagination('#page-selection', params, loadPage);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

function loadPage(event, num) {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadUsers(num, function(data) {
		loadTable(divSelector, data);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

function usersInit() {
	loadTablePage(0);
}

$(usersInit);
