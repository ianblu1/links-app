'use strict';

/* Controllers */
var linksAppControllers= angular.module('linksApp.controllers', []);

//linksAppControllers.controller('linksListController', ['$scope'] )

linksAppControllers.controller('addLinkModalController',
		['$scope', '$modalInstance', 'Bookmark', 'message', function($scope, $modalInstance, Bookmark, message){
			$scope.message=message;
			$scope.bookmark={};
			$scope.addBookmark = function(){
				//bookmark.addItem();
				Bookmark.save($scope.bookmark);
				$modalInstance.close("Link added");
			}
			$scope.cancel = function () {
		        $modalInstance.close("Nothing added");
		    };
		
		}]
		
);

linksAppControllers.controller('linksListController', 
		['$scope', '$modal', 'Bookmark', function($scope, $modal, Bookmark) {
	//$http.get('links/links.json').success(function(data) {
	//	$scope.links=data;
	//});
	$scope.bookmarks=Bookmark.query()	
	$scope.text="Hello World!";
	$scope.open= function(){
	var modalInstance = $modal.open({
	      templateUrl: 'static/partials/addLinkModal.html',
	      controller: 'addLinkModalController',
	      resolve: {
	        message: function () {
	          return $scope.text;
	        }
	      }
	    });
	modalInstance.result.then(function (paramFromModal) {
	    $scope.text = paramFromModal;
	    if (paramFromModal=="Link added"){
	    	$scope.bookmarks=Bookmark.query()
	    }
	});
	}
	
}]);



linksAppControllers.controller('linkDetailController',
		['$scope','$routeParams','$window', 'Bookmark', function($scope, $routeParams, $window, Bookmark){
			$scope.bookmark = Bookmark.get({slug:$routeParams.slug});
			$scope.update = function(bookmark){
				bookmark.$save({slug:$routeParams.slug}).then($window.location.href = '/#/links');
			}
			$scope.remove = function(bookmark){
				bookmark.$delete({slug:$routeParams.slug}).then($window.location.href = '/#/links');
			}
}]);

linksAppControllers.controller('addLinkController',
		['$scope','$routeParams','Bookmark', function($scope, $routeParams, Bookmark){
			$scope.text='Hello!';
//			$scope.bookmark = Bookmark.get({slug:$routeParams.slug});
			$scope.addBookmark = function(){
				//bookmark.addItem();
				Bookmark.save($scope.bookmark);
			}
}]);

