function getOverview(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/overview/",
	}).done(successFn).fail(errorFn);
}

function loadOverViewHTML() {
	var htmlTemplate = $("#page-wrapper .template").html();
	var output = $("#page-wrapper .dashboard-content");
	getOverview(
		function success(obj) {
			var arr = [
				//key, DisplayName, color,
				["questions", "Questions", "blue", "question-circle"],
				["answers", "Answers", "red", "comments"],
				["users", "Users", "green", "user"],
				["locations", "Locations", "grey", "map-marker"],
				["tags", "Tags", "yellow", "tag"]
			];
			var html = arr.map(function(x){
				var params = {
					number: obj[x[0]].toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,"),
					color: x[2],
					text: x[1],
					icon: x[3]
				}
				return Mustache.render(htmlTemplate, params);
			}).join('');
			output.html(html);
		},
		function fail(obj) {
			output.html("Unable to load data.");
		}
	);
}

function onload() {
	loadOverViewHTML();
}

$(document).ready(onload);

