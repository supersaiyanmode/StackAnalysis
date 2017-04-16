function viewAnswersLocalTimeInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		visualizationSelector: 'div.container-fluid div.visualization-row',
		timeChartSelector: 'div.container-fluid div.timechart-row',
		orderBySelector: 'div.container-fluid .order-by-table',
		selector: "div.container-fluid div.table-row",
		url: "/view_answers_local_time/"
	}
	tableObj = makeTable(params);
	tableObj.load();
}

$(viewAnswersLocalTimeInit);
