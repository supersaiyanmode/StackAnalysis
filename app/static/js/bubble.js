function processData(data) {
	var newDataSet = [];
	for(var prop in data) {
		newDataSet.push({name: prop, className: prop.toLowerCase(), size: data[prop]});
	}
	return {children: newDataSet};
}

function loadBubbleGraph(selector, json) {

	var diameter = 800;
	color = d3.scale.category20b(); //color category

	d3.select(selector).selectAll("*").remove();
	var svg = d3.select(selector).append('svg')
			.attr('width', diameter)
			.attr('height', diameter);

	var bubble = d3.layout.pack()
			.size([diameter, diameter])
			.value(function(d) {return d.size;}) 
			.padding(3);
  
  // generate data with calculated layout values
  var nodes = bubble.nodes(processData(json))
			.filter(function(d) { return !d.children; }); // filter out the outer bubble

	var vis = svg.selectAll('circle')
			.data(nodes);
					 
	vis.enter().append('circle')
			.attr('transform', function(d) { return 'translate(' + d.x + ',' + d.y + ')'; })
			.attr('r', function(d) { return d.r; })
			.attr('class', function(d) { return d.className; })
			.style("fill", function(d) { return color(d.value); });
			
	vis.enter().append('text')
			.attr("x", function(d){ return d.x; })
			.attr("y", function(d){ return d.y + 5; })
			.attr("text-anchor", "middle")
			.text(function(d){ return d.className + " ("+ d.value + ")"; })
			.style({
				"fill":"white", 
				"font-family":"Helvetica Neue, Helvetica, Arial, san-serif",
			})
			.style("font-size", function(d){return d.r*0.2});
}
