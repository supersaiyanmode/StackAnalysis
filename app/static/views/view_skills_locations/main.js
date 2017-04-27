function viewSkillsLocationsInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		orderBySelector: 'div.container-fluid .order-by-table',
		visualizationSelector: 'div.container-fluid div.visualization-row',
		orderBySelector: 'div.container-fluid .order-by-table',
		rowCountSelector: '.row-count-display',
		selector: "div.container-fluid div.table-row",
		url: "/view_skills_locations/"
	}
	tableObj = makeTable(params);
	tableObj.load();
}

$(viewSkillsLocationsInit);
