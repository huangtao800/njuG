function removeCropperContainer(){
	var cropper = $(".cropper-container");
	if(cropper.length>0){
		cropper.remove();
	}
}

function removeOldImg(){
	var img = $("#cropImg");
	if(img.length>0){
		img.remove();
	}
}

function createNewImg(){
	var newImg = $("<img />").attr("id", "cropImg");
	$(".cropContainer").append(newImg);
}

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
		removeCropperContainer();
		removeOldImg();
		createNewImg();
		if(this.files && this.files[0]){
	        readImage( this );
			setTimeout(function(){
			  cropImage();
			}, 50);
			$(".cropper-container").width("450px").height("400px");
			$("#cropBtn").prop("disabled",false);
			$("#uploadAvatarBtn").prop("disabled",false);
		}else{
			$("#cropBtn").prop("disabled",true);
			$("#uploadAvatarBtn").prop("disabled",true);
		}

    });
    
    $("#cropBtn").click(function(){
    	var data = $("#cropImg").cropper("getData");
    	alert(data);
    });
});
