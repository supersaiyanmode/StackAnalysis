function usersInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		visualizationSelector: 'div.container-fluid div.visualization-row',
		selector: "div.container-fluid div.table-row",
		url: "/users/"
	}
	tableObj = makeTable(params);
	tableObj.load();
}

$(usersInit);
