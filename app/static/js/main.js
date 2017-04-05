/* Template Functions */

function getTableHTML(tableData) {
	var params = {
		display: tableData.display,
		data: tableData.data.map(function(row, rowIndex) {
			var curObj = {};
			tableData.fields.forEach(function(key, index) {
				curObj[key] = row[index];
			});
			return row.map(function(cell, cellIndex) {
				var colName = tableData.fields[cellIndex];
				var colPostProc = tableData.mappers[colName]
				if (colPostProc === undefined) {
					return {
						type_text: "type_text",
						value: cell
					}; 
				} else if (colPostProc.type == "link_replace") {
					var result = {
						type_link_replace: "link_replace",
						url: Handlebars.compile(colPostProc.url)(curObj),
						replace: colPostProc.replace,
						value: cell
					};
					return result;
				} else if (colPostProc.type == "link_open") {
					var result = {
						type_link_open: "link_open",
						url: Handlebars.compile(colPostProc.url)(curObj),
						value: cell
					};
					return result;
				}
			});
		})
	};
	var template = $("script#table-template").html();
	return Handlebars.compile(template)(params);
}

function loadTable(selector, tableData) {
	var html = getTableHTML(tableData);
	$(selector).on("click", "a.dyn-link-replace", function() {
		var element = $(this);
		$.ajax({
			url: element.data('href'),
			type: "GET"
		}).done(function(data) {
			var template = element.data('replace');
			var val = Handlebars.compile(template)(data);
			element[0].outerHTML = val;
		}).fail(function(data) {
			//nothing.
		});
	});

	$(selector).html(html);
}


/* Nagivation relation stuff. */
function getQueries(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/views/",
	}).done(successFn).fail(errorFn);
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
		$("ul.nav.navbar-nav.side-nav li.active").removeClass("active");
		var view = $(this).data("view");
		$(this).closest('li').addClass("active");
		$.get("/static/views/" + view + "/page.html", function (data) {
			$("#page-wrapper").html(data);
		})
	})
	setTimeout(function() {
		$("ul.nav.navbar-nav.side-nav li:first-child").addClass("active");
		$("ul.nav.navbar-nav.side-nav li a")[0].click();
	}, 10)
}

$(document).ready(loadNavigation);

