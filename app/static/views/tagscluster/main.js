function loadTagsCluster(data) {

}

function tagsClusterInit() {
	$.ajax({
		url: '/tagscluster/',
		type: 'GET'
	}).done(loadTagsCluster).fail(function() {
		alert("Failed to load.");
	});
}

$(tagsClusterInit);
