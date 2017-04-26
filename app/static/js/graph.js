

function graphPreprocess(data) {
	var nodesArr =  [].concat.apply(Object.keys(data), Object.values(data).map(Object.keys));
	nodes = nodesArr.map(function(x) { return {name: x, group: 0}; });

	var links = [];
	Object.keys(data).forEach(function (tag1) {
		var value = data[tag1];
		var tag1Id = nodesArr.indexOf(tag1);
		Object.keys(value).forEach(function (tag2) {
			probVal = value[tag2];
			links.push({
				source: tag1Id,
				target: nodesArr.indexOf(tag2),
				weight: probVal.prob
			});
		});
	})
	return {nodes: nodes, links: links};
}

function loadGraph(selector, data, params) {
	var json = graphPreprocess(data);

	var params = params || {};
	var width = params.width || 500;
	var height = params.height || 500;

	d3.select(selector).selectAll("*").remove();
	var svg = d3.select(selector).append("svg")
	    .attr("width", "100%")
	    .attr("height", "800px");

	var force = d3.layout.force()
	    .gravity(.05)
	    .distance(100)
	    .charge(-100)
	    .size([width, height]);

	force
		.nodes(json.nodes)
		.links(json.links)
		.start();

	var link = svg.selectAll(".link")
				.data(json.links)
				.enter().append("line")
	  			.attr("class", "link")
	  			.style("stroke", "#aaa")
				.style("stroke-width", function(d) {
					return Math.sqrt(d.weight); 
				});

	var node = svg.selectAll(".node")
	  			.data(json.nodes)
				.enter().append("g")
	  			.attr("class", "node")
	  			.call(force.drag);

	node.append("circle")
				.attr("r","5")
				.style("stroke", "#fff")
				.style("stroke-width", "3px")
				.style("fill", "#555");

	node.append("text")
				.attr("dx", 12)
				.attr("dy", ".35em")
				.style("stroke", "#333")
				.text(function(d) { return d.name });

	force.on("tick", function() {
		link.attr("x1", function(d) { return d.source.x; })
		    .attr("y1", function(d) { return d.source.y; })
		    .attr("x2", function(d) { return d.target.x; })
		    .attr("y2", function(d) { return d.target.y; });

		node.attr("transform", function(d) {
			return "translate(" + d.x + "," + d.y + ")";
		});
	});
}