function viewAnswersLocalTimeInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		visualizationSelector: 'div.container-fluid div.visualization-row div.row',
		timeChartSelector: 'div.container-fluid div.timechart-row div.row',
		selector: "div.container-fluid div.table-row div.row",
		url: "/view_answers_local_time/"
	}
	tableObj = makeTable(params);
	tableObj.load();
}

$(viewAnswersLocalTimeInit);
