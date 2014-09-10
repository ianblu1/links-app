'use strict';


// Declare app level module which depends on filters, and services
angular.module('linksApp', [
  'ngRoute',
  'ui.bootstrap',
  'linksApp.controllers',
  'linksApp.services'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/links', {
	  	templateUrl: 'static/partials/list.html', 
	  	controller: 'linksListController'
	  }).
	  when('/links/:slug', {
		templateUrl: 'static/partials/link_detail.html',
		controller: 'linkDetailController'
	  }).
	  when('/add_link',{
		 templateUrl: 'static/partials/add_link.html',
		 controller: 'addLinkController'
	  }).
	  otherwise({
		  redirectTo: '/links'
	  });
}]);