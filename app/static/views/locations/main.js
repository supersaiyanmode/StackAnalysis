function locationsInit() {
	var params = {
		paginationSelector: 'div.container-fluid .pagination-bar',
		queryFilterSelector: 'div.container-fluid .filter-query-table',
		visualizationSelector: 'div.container-fluid div.visualization-row div.row',
		selector: "div.container-fluid div.table-row div.row",
		url: "/locations/"
	}
	tableObj = makeTable(params);
	tableObj.load();
	$('#div.container-fluid div.visualization-row div.row').on("classChanged",function() {
			showVisualization();
		});
}

function showVisualization () {
	google.charts.load('current', {'packages':['corechart']});
	google.charts.setOnLoadCallback(drawVisualization);

	function drawVisualization (){
		
		var data = google.visualization.arrayToDataTable([
				['Time', 'Frequency'],
				[new Date(0,0,0,12,0,0),  165],
				[new Date(0,0,0,1,30,0),  135],
				[new Date(0,0,0,2,24,0),  157],
				[new Date(0,0,0,7,16,0),  139],
				[new Date(0,0,0,7,0,0),  136]
				]);
				 var ar  = new Array();
				for(var i=0;i<24;i++)
				{
					ar.push(new Date(0,0,0,i,0,0));
					ar.push(new Date(0,0,0,i,30,0));
				}
				var options = {
					title : 'Example',
					vAxis: {title: 'Frequency'},
					hAxis: {
						title: 'Time', format:'HH:mm:ss',
						gridlines:	{
								units:	{
										hours: {format: ['HH:mm', 'ha']}
										}
									},
						ticks: ar
					},
					seriesType: 'bars',
					series: {3: {type: 'line'}}
		};
		var chart = new google.visualization.ComboChart(document.getElementById('timeline'));
		chart.draw(data, options);
	}
}
	

$(locationsInit);
