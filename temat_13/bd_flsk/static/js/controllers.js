var galleryApp=angular.module('galleryApp',[]);



galleryApp.controller('GalleryListCtrl',['$scope','$http'],function($scope, $http){
	
	
	$http.get('json/galleries.json').success(function(data) {$scope.galleries=data;});
	
	
	$scope.sectionname='Galeria';
	$scope.date= new Date();
	$scope.sortList = [
		{
		'label':'Alfabetycznie',
		'value':'title'
		},
		{
		'label':'Chronologicznie',
		'value':'when'
		},
		{
		'label':'Od najnowszej',
		'value':'-when'
		}
		]; 
	$scope.orderProp='when';
	
		
});


	
	
	


