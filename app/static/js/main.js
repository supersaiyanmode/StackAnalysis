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
			return Mustache.render(listItemTemplate, params);
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
