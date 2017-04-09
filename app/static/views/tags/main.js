function tagsInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		selector: "div.container-fluid div.table-row div.row",
		url: "/tags/"
	}
	tableObj = makeTable(params);
	tableObj.load();
}

$(tagsInit);