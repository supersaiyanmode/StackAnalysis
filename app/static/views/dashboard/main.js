function getOverview(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/overview/",
	}).done(successFn).fail(errorFn);
}

function loadOverViewHTML() {
	var htmlTemplate = $("#overview-template").html();
	var output = $("#page-wrapper .dashboard-content");
	getOverview(
		function success(obj) {
			var html = obj.data.map(function(x){
				x.sub = JSON.stringify(x.sub);
				x.number = x.number.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
				return Handlebars.compile(htmlTemplate)(x);
			}).join('');
			output.html(html);
		},
		function fail(obj) {
			output.html("Unable to load data.");
		}
	);

	$("#page-wrapper .dashboard-content").on("click", "a", function() {
		var view = $(this).data('view');
		var sub = $(this).data('sub');
		setCentralView(view, sub);
	});
}

function onload() {
	loadOverViewHTML();
}

$(document).ready(onload);
//# sourceURL=dashboard.js
