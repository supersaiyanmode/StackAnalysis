function usersMultipleTagsInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		visualizationSelector: 'div.container-fluid div.visualization-row',
		timeChartSelector: 'div.container-fluid div.timechart-row',
		selector: "div.container-fluid div.table-row",
		url: "/users_multiple_tags/"
	}
	tableObj = makeTable(params);
	tableObj.load();
}

$(usersMultipleTagsInit);
