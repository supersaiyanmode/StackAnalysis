function getOverview(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/overview/",
	}).done(successFn).fail(errorFn);
}
