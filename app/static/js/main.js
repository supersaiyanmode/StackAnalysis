
/* Nagivation relation stuff. */
function getQueries(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/views/",
	}).done(successFn).fail(errorFn);
}

function setCentralView(view) {
	$("ul.nav.navbar-nav.side-nav li.active").removeClass("active");
	$("ul.nav.navbar-nav.side-nav li a[data-view='" + view + "']").parent().addClass("active");
	$.get("/static/views/" + view + "/page.html", function (data) {
		$("#page-wrapper").html(data);
	});
}

function loadNavigation() {
	var listItemTemplate = $("ul.nav.navbar-nav.side-nav").html();
	var output = $("ul.nav.navbar-nav.side-nav");

	getQueries(function(obj) {
		var fields = obj.fields;
		var data = obj.data;
		var html = data.map(function(x) {
			var params = {
				text: x[0],
				view: x[1],
				icon: x[2]
			};
			var template = Handlebars.compile(listItemTemplate);
			return template(params);
		}).join("");
		output.html(html);
	}, function(obj) {
		output.html("Unable to load data.");
	});
	
	$("ul.nav.navbar-nav.side-nav").on("click", "li a", function() {
		var view = $(this).data("view");
		setCentralView(view);
	})
	setTimeout(function() {
		setCentralView('dashboard');
	}, 10)
}


/* map related stuff. */
function drawRegionsMap(selector, dataList, title, options) {
	dataList.unshift(title);
	var data = google.visualization.arrayToDataTable(dataList);
	if (options === undefined) {
		options = {};
	}
	var element = $(selector)[0];
	var chart = new google.visualization.GeoChart(element);
	chart.draw(data, options);
}


function drawTimeDistribution(selector, dataList, title, options) {
	dataList.unshift(title);
	var data = google.visualization.arrayToDataTable(dataList);
	if (options === undefined) {
		options = {};
	}
	var element = $(selector)[0];
	var chart = new google.visualization.ComboChart(element);
	chart.draw(data, options);

}
$(document).ready(loadNavigation);


