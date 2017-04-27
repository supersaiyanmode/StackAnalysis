
/* Nagivation relation stuff. */
function getQueries(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/views/",
	}).done(successFn).fail(errorFn);
}

function setCentralView(view, sub, hash) {
	$("ul.nav.navbar-nav.side-nav li.active").removeClass("active");
	$("ul.nav.navbar-nav.side-nav li a[href='#" + hash + "']").parent().addClass("active");
	$.get(view, function (data) {
		var html = Handlebars.compile(data)(sub);
		$("#page-wrapper").html(html);
	});
}

function loadRoutes(data) {
	data.forEach(function(x) {
		crossroads.addRoute(x.hashurl, function() {
			setCentralView(x.view, x.sub, x.hashurl);
		});
	});

	//setup hasher
	function parseHash(newHash, oldHash){
		crossroads.parse(newHash);
	}
	hasher.initialized.add(parseHash); // parse initial hash
	hasher.changed.add(parseHash); //parse hash changes
	hasher.init(); //start listening for history change
}

function loadNavigation() {
	var listItemTemplate = $("ul.nav.navbar-nav.side-nav").html();
	var output = $("ul.nav.navbar-nav.side-nav");
	var template = Handlebars.compile(listItemTemplate);

	getQueries(function(obj) {
		var html = obj.data.map(function(x) {
			return x.hashparam? "": template(x);
		}).join("");
		output.html(html);
		
		loadRoutes(obj.data);
		
		setTimeout(function() {
			hasher.setHash('/');
		}, 10);
	}, function(obj) {
		output.html("Unable to load data.");
	});
}


/* map related stuff. */
function drawRegionsMap(selector, dataList, title, opts) {
	dataList = dataList.slice();
	dataList.unshift(title);
	var data = google.visualization.arrayToDataTable(dataList);
	var options = {
		displayMode: "markers",
		height: 480,
		colorAxis: {colors: ['red','blue']}
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

function drawMultiBarDistribution (selector, dataList, title, opts){
	var data = dataList.slice();
	data.unshift(title);
	data = google.visualization.arrayToDataTable(data);
	var options = {
		title : 'Reputation vs Fake Locations',
		vAxis: {title: 'Locations'},
		hAxis: {title: 'Reputation'},
		seriesType: 'bars',
		series: {5: {type: 'line'}},
		height: 480
	};
	if (opts !== undefined) {
		$.extend(options, opts);
	}

	var element = $(selector)[0];
	var chart = new google.visualization.ComboChart(element);
	chart.draw(data, options);
}

function drawMultipleTagsBarDistribution (selector, dataList, title, opts){
	var data = dataList.slice();
	data.unshift(title);
	data = google.visualization.arrayToDataTable(data);
	var options = {
		title: 'Users Contribution In Multiple tags',
		height: 480,
		seriesType: 'bars',
		series: {5: {type: 'line'}}
	};

	if (opts !== undefined) {
		$.extend(options, opts);
	}

	var element = $(selector)[0];
	var chart = new google.visualization.ComboChart(element);
	chart.draw(data, options);
}

$(document).ready(loadNavigation);


