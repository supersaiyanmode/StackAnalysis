function makeTable(params) {
	var tableSelector = params.selector;
	var paginationSelector = params.paginationSelector;
	var queryFilterSelector = params.queryFilterSelector;
	var tableUrl = params.url;
	var tableFilterData = [];
	var tableLoaded  = false;
	
	function processCellContents(cell, curObj, colPostProc) {
		if (colPostProc === undefined) {
			return {
				type_text: "type_text",
				value: cell
			};
		} else if (colPostProc.type == "link_replace") {
			return {
				type_link_replace: "link_replace",
				url: Handlebars.compile(colPostProc.url)(curObj),
				replace: colPostProc.replace,
				vapaginationSelectorlue: cell
			};
		} else if (colPostProc.type == "link_open") {
			return {
				type_link_open: "link_open",
				url: Handlebars.compile(colPostProc.url)(curObj),
				value: cell
			};
		}
	}
	
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
					return processCellContents(cell, curObj, colPostProc);
				});
			})
		};
		var template = $("script#table-template").html();
		return Handlebars.compile(template)(params);
	}
	
	function fetchTableData(url, filter, page, successFn, errorFn) {
		var getParams = {};
		if (filter != null) {
			getParams.filter = JSON.stringify(filter);
		}
		if (page != null) {
			getParams.page = page;
		}
		$.ajax({
			type: "GET",
			url: url,
			data: getParams
		}).done(successFn).fail(errorFn);
	}
	
	function attachTableContentEvents() {
		//Link-Replace
		$(tableSelector).on("click", "a.dyn-link-replace", function() {
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
	}
	
	function loadPagination(tableData) {
		var paginationParams = {
			total: Math.ceil(tableData.meta.rows / tableData.meta.page_size),
			maxVisible: 10
		};
		$(paginationSelector).bootpag(paginationParams).on("page", function(event, pageNumber) {
			renderTableWithParams(pageNumber - 1, tableFilterData);
		});
	}
	
	function enableVisualizationsButton() {
		$(".btn-group > a.btn.disabled").removeClass("disabled");
		$('.btn-group a.btn').on('click', function(){
			$(this).parent().find('.active').removeClass('active');
			$(this).addClass('active');

			var panelClass = $(this).data("panel-class");
			$("div.tab-pane.active").removeClass("active");
			$("." + panelClass).parent().addClass("active");
		});
	}

	function renderTableWithParams(page, filter) {
		fetchTableData(tableUrl, filter, page, function(tableData) {
			$(tableSelector).html(getTableHTML(tableData));
			if (tableLoaded == false) {
				attachTableContentEvents();
				loadFilterQueryView(tableData);
				attachTableQueryFilterEvents(tableData);
				tableLoaded = true;
			}
			$(paginationSelector).unbind('page');
			loadPagination(tableData);

			//check for tableData.location
			if (tableData.location !== undefined) {
				enableVisualizationsButton();
			}
		}, function() {
			$(tableSelector).html("Failed to load data.");
		});
	}
	
	function loadFilterQueryView(tableData) {
		var templateTable = $("#filter-table-template").html();
		var tableParams = {
			filterJSON: JSON.stringify(tableData.filter)
		};

		var html = Handlebars.compile(templateTable)(tableParams);
		var tableNode = $.parseHTML(html);
		$(queryFilterSelector).append(tableNode);

		addRowFilterQuery(queryFilterSelector, tableData);
	}
	
	function addRowFilterQuery(selector, tableData) {
		var templateRow = $("#filter-table-row-template").html();
		var html = Handlebars.compile(templateRow)(tableData);
		var rowNode = $.parseHTML(html);
		$(queryFilterSelector + " table tbody").append(rowNode);
	}

	function attachTableQueryFilterEvents(tableData) {
		$(queryFilterSelector).on("click", "button.query-filter-add", function() {
			addRowFilterQuery(tableSelector, tableData);
		});
	
		$(queryFilterSelector).on("click", "button.query-filter-go", function() {
			var obj = $(queryFilterSelector + " tbody tr").map(function() {
				var colSel = $(this).find(".query-filter-column-select option:selected");
				var opSel = $(this).find(".query-filter-op-select option:selected");
				var inp = $(this).find("input[name=operand]");
				return {
					col: colSel.attr("value"),
					op: opSel.attr("value"),
					val: inp.val()
				};
			}).get();
			tableFilterData = obj; //global variable update.
			renderTableWithParams(0, tableFilterData);
		});
	
		$(queryFilterSelector).on("change", "select.query-filter-column-select", function() {
			var table = $(this).closest('table');
			var filt = table.data("ops");
			var row = $(this).closest('tr');
			var curId = $(this).find("option:selected").attr('value');
			var curCol = filt.filter(function (x) { return x.id == curId; });
			if (curCol.length == 0)
				return;

			var curCol = curCol[0];
			var opsSelect = row.find(".query-filter-op-select");
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
	
	return {
		load: function() {
			tableFilterData = [];
			renderTableWithParams(0, tableFilterData);
		}
	}
}
