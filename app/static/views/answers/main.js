function answersInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		selector: "div.container-fluid div.table-row div.row",
		url: "/answers/"
	}
	tableObj = makeTable(params);
	tableObj.load();
}

$(answersInit);
