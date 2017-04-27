function viewPostsCountLocationsInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		visualizationSelector: 'div.container-fluid div.visualization-row',
		selector: "div.container-fluid div.table-row",
		rowCountSelector: '.row-count-display',
		url: "/view_posts_count_locations/"
	}
	tableObj = makeTable(params);
	tableObj.load();
}

$(viewPostsCountLocationsInit);
