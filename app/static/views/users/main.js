function usersInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		orderBySelector: 'div.container-fluid .order-by-table',
		visualizationSelector: 'div.container-fluid div.visualization-row',
		orderBySelector: 'div.container-fluid .order-by-table',
		selector: "div.container-fluid div.table-row",
		url: "/users/"
	}
	tableObj = makeTable(params);
	tableObj.load();
}

$(usersInit);
