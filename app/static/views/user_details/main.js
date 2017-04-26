function getUserDetails(successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/questions/",
		data:{author_id :123}
	}).done(successFn).fail(errorFn);
}

function loadUserQuestiondetails() {
	var filterStr = [
		["filter", JSON.stringify([{
			"col": "author_id",
			"op": "__eq__",
			"val": "123"
			}])],
		["sort", JSON.stringify([{
			"col": "score",
			"order": "desc"
		}])]
	].map(function(item) {
		return item[0] + "=" + encodeURIComponent(item[1]);
	}).join("&");

	var params = {
		paginationSelector: 'div.container-fluid .pagination1-bar',
		selector: 'div.container-fluid div.questions-content',
		url: "/questions/?" +filterStr 
	}
	getUserDetails(
		function success(obj) {
			var tableObj = makeTable(params);
			tableObj.load();
		},
		function fail(obj) {
			$('#user-content').html("Unable to load data.");
		}
	);
	


}

function loadUserAnswerdetails() {
	var filterStr = [
		["filter", JSON.stringify([{
			"col": "author_id",
			"op": "__eq__",
			"val": "123"
			}])],
		["sort", JSON.stringify([{
			"col": "score",
			"order": "desc"
		}])]
	].map(function(item) {
		return item[0] + "=" + encodeURIComponent(item[1]);
	}).join("&");

	var params = {
		paginationSelector: 'div.container-fluid .pagination2-bar',
		selector: 'div.container-fluid div.answers-content',
		url: "/answers/?" +filterStr 
	}
	getUserDetails(
		function success(obj) {
			var tableObj = makeTable(params);
			tableObj.load();
		},
		function fail(obj) {
			$('#user-content').html("Unable to load data.");
		}
	);
	


}


function onload() {
	loadUserQuestiondetails();
	loadUserAnswerdetails();
}

$(document).ready(onload);
//# sourceURL=dashboard.js
