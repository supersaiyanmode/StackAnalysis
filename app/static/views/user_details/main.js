function loadUserInfoDetails(userId, successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/users/" + userId + "/"
	}).done(successFn).fail(errorFn);
}

function loadLocationInfoDetails(locId, successFn, errorFn) {
	$.ajax({
		type: "GET",
		url: "/locations/" + locId + "/"
	}).done(successFn).fail(errorFn);
}

function loadUserTagDetails(userId, successFn, errorFn) {
	var url = "/users_tags/?filter=%5B%7B%22col%22%3A%22user_id" + 
				"%22%2C%22op%22%3A%22__eq__%22%2C%22val%22%3A" + userId + 
				"%7D%5D&sort=%5B%7B%22col%22%3A%22answer_count" +
				"%22%2C%22order%22%3A%22desc%22%7D%5D&page=0";
	$.ajax({
		type: "GET",
		url: url
	}).done(successFn).fail(errorFn);
}

function loadUserInfo(data) {
	$(".user-name").html(data.name);
	$(".user-reputation").html(data.reputation);
	$(".user-image").html('<img class="img-responsive page-header" src="/users/' + data.id + '/dp" />');
	loadLocationInfoDetails(data.location_id, loadLocationInfo, null);
}

function loadLocationInfo(data) {
	$(".user-location").html(data.location);
	var location = [data.city, data.state, data.country].map(function(x) {
			return x || "";
		}).filter(function(x) { return !!x; }).join(", ");
	if (location) {
		$(".user-resolved-location").html("(" + location + ")");
	}
}

function loadUserTags(userId) {
	loadUserTagDetails(userId, function(obj) {
		var json = {};
		var data = obj["data"]
		for(var item in data) {
			json[data[item][1]] = data[item][2];
		}
		
		var params = {
			diameter: 300
		};
		loadBubbleGraph('.user-tags', json, params);
	}, function(data) { alert("Failed to load data."); });
}

function loadUserQuestiondetails(userId) {
	var params = {
		paginationSelector: 'div.container-fluid .questions-section .pagination-bar',
		selector: "div.container-fluid .questions-section div.table-row",
		rowCountSelector: '.questions-section .row-count-display',
		baseSelector: '.questions-section',
		url: "/questions/",
		tableOrderData: [{"col": "score", "order": "desc"}],
		tableFilterData: [{
			"col": "author_id",
			"op": "__eq__",
			"val": userId
		}],
		maxPages:5
	};
	var tableObj = makeTable(params);
	tableObj.load();
}

function loadUserAnswerdetails(userId) {
	var selector = 'div.container-fluid .answers-section .table-content';
	var params = {
		paginationSelector: 'div.container-fluid .answers-section .pagination-bar',
		selector: "div.container-fluid .answers-section div.table-row",
		rowCountSelector: '.answers-section .row-count-display',
		baseSelector: '.answers-section',
		url: "/answers/",
		tableOrderData: [{"col": "score", "order": "desc"}],
		tableFilterData: [{
			"col": "author_id",
			"op": "__eq__",
			"val": userId
		}],
		maxPages:5
	};
	var tableObj = makeTable(params);
	tableObj.load();
}


function onload() {
	var match = location.hash.match(/#\/user-details\/(.*)/);
	if (!match) {
		alert("Invalid hash.");
		return;
	}
	var userId = match[1];
	loadUserQuestiondetails(userId);
	loadUserAnswerdetails(userId);
	loadUserInfoDetails(userId, loadUserInfo, function(data) {alert("Error..");});
	loadUserTags(userId);
}

$(document).ready(onload);
//# sourceURL=user_details.js
