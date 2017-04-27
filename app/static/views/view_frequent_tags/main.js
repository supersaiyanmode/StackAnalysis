function getResponse(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/view_frequent_tags/",
	}).done(successFn).fail(errorFn);
}

function viewFrequentTagsInit() {
	getResponse(
		function success(obj) {
			var json ={};
			var selector = ".container-fluid .frequent-tags";
			var data = obj["data"]
			for(var item in data){
				json[data[item][1]] = data[item][2];
			}
			loadBubbleGraph(selector, json, {})
		},
		function fail(obj) {
			$(selector).html("Failed to load data")
		}
	);
}

$(viewFrequentTagsInit);
