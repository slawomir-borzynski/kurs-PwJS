var galleryApp=angular.module('galleryApp',[]);



galleryApp.controller('GalleryListCtrl',function($scope){
	$scope.sectionname='Galeria'
	$scope.date= new Date();
	$scope.galleries=[
		{
			'title':'Zdjęcie 1',
			'when':'2019-06-23',
			'thumbnailUrl':'img/galeria/picture1.jpg'
		},
		{
			'title':'Zdjęcie 2',
			'when':'2017-04-15',
			'thumbnailUrl':'img/galeria/picture2.jpg'
		},
		{
			'title':'Zdjęcie 3',
			'when':'2018-10-13',
			'thumbnailUrl':'img/galeria/picture3.jpg'
		},
		{
			'title':'Zdjęcie 4',
			'when':'2015-09-11',
			'thumbnailUrl':'img/galeria/picture4.jpg'
		},
		{
			'title':'Zdjęcie 5',
			'when':'2016-06-13',
			'thumbnailUrl':'img/galeria/placehold/placeholder.jpg'
		},
		{
			'title':'Zdjęcie 6',
			'when':'2010-06-13',
			'thumbnailUrl':'img/galeria/picture5.jpg'
		},
		{
			'title':'Zdjęcie 7',
			'when':'2010-05-03',
			'thumbnailUrl':'img/galeria/placehold/placeholder.jpg'
		},
		{
			'title':'Zdjęcie 8',
			'when':'2012-04-16',
			'thumbnailUrl':'img/galeria/placehold/placeholder.jpg'
		},
		{
			'title':'Zdjęcie 9',
			'when':'2011-07-23',
			'thumbnailUrl':'img/galeria/placehold/placeholder.jpg'
		},
		
		
		
	]
	

});


	
	
	


