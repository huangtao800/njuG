function readImage(input) {
    if ( input.files && input.files[0] ) {
        var FR= new FileReader();
        FR.onload = function(e) {
             $('#cropImg').attr( "src", e.target.result );
        };       
        FR.readAsDataURL( input.files[0] );
    }
}

function cropImage(){
	$("#cropImg").cropper({
	  aspectRatio: 1 / 1,
	  autoCropArea: 0.8,
	  strict: true,
	  guides: false,
	  highlight: false,
	  dragCrop: false,
	  cropBoxMovable: false,
	  cropBoxResizable: false
	});
}

$(document).ready(function(){
    $("#avatarInput").change(function(){
    	var cropper = $(".cropper-container");
    	if(cropper.length>0){
    		cropper.remove();
    		var img = $("#cropImg");
    		img.remove();
    		var newImg = $("<img />").attr("id", "cropImg");
    		$(".cropContainer").append(newImg);
    	}
        readImage( this );
		setTimeout(function(){
		  cropImage();
		}, 100);
		// setTimeout(function(){
			// $(".cropper-container").attr("width", "400px").attr("height", "400px");
		// },100);
		$(".cropper-container").width("450px").height("400px");
		
    });
    // cropImage();
});
