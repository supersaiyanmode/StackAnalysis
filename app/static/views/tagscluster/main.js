function loadTagsCluster(data) {
	var selector = ".container-fluid .tags-cluster";
	var params = {};
	loadGraph(selector, data.result, params);
}

function tagsClusterInit() {
	$.ajax({
		url: '/tags_cluster/',
		type: 'GET'
	}).done(loadTagsCluster).fail(function() {
		alert("Failed to load.");
	});
}

$(tagsClusterInit);
