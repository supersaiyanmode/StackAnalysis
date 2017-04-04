function loadUsers(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/users/"
	}).done(successFn).fail(errorFn);
}

function usersInit() {
	var divSelector = "div.container-fluid div.table-row div.row";
	loadUsers(function(data) {
		var html = getTableHTML(data);
		$(divSelector).html(html);
	}, function(data) {
		$(divSelector).html("Unable to load data.");
	});
}

$(usersInit);
