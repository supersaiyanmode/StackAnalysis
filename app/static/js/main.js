
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
function drawRegionsMap(selector, dataList, title, opts) {
	dataList = dataList.slice();
	dataList.unshift(title);
	var data = google.visualization.arrayToDataTable(dataList);
	var options = {
		displayMode: "markers",
		height: 480
	};
	
	if (opts !== undefined) {
		$.extend(options, opts);
	}

	var element = $(selector)[0];
	var chart = new google.visualization.GeoChart(element);
	chart.draw(data, options);
}

function drawTimeDistribution(selector, dataList, title, opts) {
	dataList = dataList.map(function(obj) {
		obj[0] = new Date(0, 0, 0, obj[0], 0, 0, 0);
		return obj;
	});
	
	var allHours = dataList.map(function (_, i) {
		return new Date(0, 0, 0, i, 0, 0, 0);
	});
	
	dataList.unshift(title);
	var data = google.visualization.arrayToDataTable(dataList);
	var options = {
		vAxis: {title: 'Frequency'},
		hAxis: {
			title: 'Time',
			format:'HH',
			gridlines: {
				units: {
					hours: {format: ['HH', 'ha']}
				}
			},
			ticks: allHours
		},
		height: 480,
		seriesType: 'bars',
		series: {3: {type: 'line'}}
	};
	
	if (opts !== undefined) {
		$.extend(options, opts);
	}

	var element = $(selector)[0];
	var chart = new google.visualization.ComboChart(element);
	chart.draw(data, options);
}

$(document).ready(loadNavigation);


