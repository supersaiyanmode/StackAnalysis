function getQueries(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/queries/",
	}).done(successFn).fail(errorFn);
}

function loadNavigation() {
	var listItemTemplate = $("#navbartemplate").html();
	var output = $("ul.nav.navbar-nav.side-nav");

	var icons = {
		"Dashboard": "dashboard"
	}

	getQueries(function(obj) {
		var fields = obj.fields;
		var data = obj.data;
		var html = data.map(function(x) {
			var params = {
				text: x[0],
				url: x[1],
				icon: icons[x[0]]
			};
			return Mustache.render(listItemTemplate, params);
		}).join("");
		//output.html(html);
	}, function(obj) {
		output.html("Unable to load data.");
	});
}

$(document).ready(loadNavigation);
