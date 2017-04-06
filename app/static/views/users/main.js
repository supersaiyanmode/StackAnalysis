function loadUsers(page, filter, successFn, errorFn) {
	var filt = "";
	if (filter != null) {
		filt = "&filter=" + encodeURIComponent(filter);
	}
	$.ajax({
		type: "GET",
		url: "/users/?page=" +page + filt
	}).done(successFn).fail(errorFn);
}

function loadTablePage(num) {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadUsers(num, null, function(data) {
		loadTable(divSelector, data);
		var params = {
			total: Math.ceil(data.meta.rows / data.meta.page_size),
			maxVisible: 10
		};
		loadPagination('#page-selection', params, loadPage);
		loadFilterQuery('div.container-fluid .filter-query-table', data, updateUserFilter);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

function loadPage(event, num) {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadUsers(num, null, function(data) {
		loadTable(divSelector, data);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

function usersInit() {
	loadTablePage(0);
}

function updateUserFilter(obj) {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadUsers(0, JSON.stringify(obj), function(data) {
		loadTable(divSelector, data);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

$(usersInit);
