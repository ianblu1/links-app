/* Services */
var linksAppServices=angular.module('linksApp.services', ['ngResource']);

linksAppServices.factory('Bookmark', ['$resource',
  function($resource){
    return $resource('data/:slug', {}, {
      query: {method:'GET', params:{slug:'bookmarks'}, isArray:true}
    
    });
  }]);