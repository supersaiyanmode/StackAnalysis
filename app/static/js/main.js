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

/* Pagination related stuff. */

function loadPagination(selector, params, func) {
	$(selector).bootpag(params).on("page", func);
}


/* Filter Query related stuff. */
function addRowFilterQuery(selector, params) {
	var templateRow = $("#filter-table-row-template").html();
	var html = Handlebars.compile(templateRow)(params);
	var rowNode = $.parseHTML(html);
	
	$(selector + " table tbody").append(rowNode);
}

function loadFilterQuery(selector, params, func) {
	var templateTable = $("#filter-table-template").html();
	var tableParams = {
		filterJSON: JSON.stringify(params.filter)
	};

	var html = Handlebars.compile(templateTable)(tableParams);
	var tableNode = $.parseHTML(html);
	$(selector).append(tableNode);

	addRowFilterQuery(selector, params);
	
	$(selector).on("click", "button.query-filter-add", function() {
		addRowFilterQuery(selector, params);
	});
	
	$(selector).on("click", "button.query-filter-go", function() {
		var obj = $(selector + " tbody tr").map(function() {
			var colSel = $(this).find(".query-filter-column-select option:selected");
			var opSel = $(this).find(".query-filter-op-select option:selected");
			var inp = $(this).find("input[name=operand]");
			return {
				col: colSel.attr("value"),
				op: opSel.attr("value"),
				val: inp.val()
			};
		}).get();
		func(obj);
	});
	
	$(selector).on("change", "select.query-filter-column-select", function() {
		var table = $(this).closest('table');
		var filt = table.data("ops");
		var curId = $(this).find("option:selected").attr('value');
		var curCol = filt.filter(function (x) { return x.id == curId; });
		if (curCol.length == 0)
			return;

		var curCol = curCol[0];
		var opsSelect = table.find(".query-filter-op-select");
		opsSelect.html("");
		opsSelect.prop("disabled", false);
		curCol.valid_ops.forEach(function(x) {
			opsSelect.append($('<option>', { 
				value: x.id,
				text : x.text 
			}));
		});
	});
}


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

$(document).ready(loadNavigation);


