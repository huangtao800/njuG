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

function uplpadAvatar(){
	if($("#cropImg").attr("src")){
		var x = $("#cropImg").cropper("getData")['x'];
		var y = $("#cropImg").cropper("getData")['y'];
		var width = $("#cropImg").cropper("getData")['width'];
		var height = $("#cropImg").cropper("getData")['height'];
		var imgContent = $("#cropImg").attr("src");
		var imgName = $("#avatarInput").val().split('\\').pop();
		$.ajax({
			url: "/njuG/postAvatar/",
			dataType: "json",
			headers: { "X-CSRFToken": $.cookie("csrftoken") },
			type: 'POST',
			data: {"x": x, "y":y, "width":width, "height":height, "imgName": imgName, "imgContent": imgContent},
			success: function(response){
				alert("success");
			},
		});
	}
	return false;
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
    	$("img.avatarPreview").attr("src", $("#cropImg").attr("src"));
    	
    	var cropBoxWidth = $("#cropImg").cropper("getCropBoxData")['width'];
    	var cropBoxTop = $("#cropImg").cropper("getCropBoxData")['top'] - $("#cropImg").cropper("getCanvasData")['top'];
    	var cropBoxLeft = $("#cropImg").cropper("getCropBoxData")['left'] - $("#cropImg").cropper("getCanvasData")['left'];
    	
    	var imgNaturalWidth = $("#cropImg").cropper("getImageData")['naturalWidth'];
    	var imgNaturalHeight = $("#cropImg").cropper("getImageData")['naturalHeight'];
    	var imgWidth = $("#cropImg").cropper("getImageData")['width'];
    	var imgHeight = $("#cropImg").cropper("getImageData")['height'];
    	
    	var largeRatio = $(".largeAvatar").width() / cropBoxWidth;
    	var largeImgWidth = largeRatio * imgWidth;
    	var largeImgHeight = largeRatio * imgHeight;
    	$(".largeAvatarImg").width("" + largeImgWidth + "px");
    	$(".largeAvatarImg").height("" + largeImgHeight + "px");
    	$(".largeAvatarImg").css({top: "-"+largeRatio*cropBoxTop+"px", left:"-"+largeRatio*cropBoxLeft+"px"});
    	
    	var middleRatio = $(".middleAvatar").width() / cropBoxWidth;
    	var middleImgWidth = middleRatio * imgWidth;
    	var middleImgHeight = middleRatio * imgHeight;
    	$(".middleAvatarImg").width("" + middleImgWidth + "px");
    	$(".middleAvatarImg").height("" + middleImgHeight + "px");
    	$(".middleAvatarImg").css({top: "-"+middleRatio*cropBoxTop+"px", left:"-"+middleRatio*cropBoxLeft+"px"});
    	
    	var smallRatio = $(".smallAvatar").width() / cropBoxWidth;
    	var smallImgWidth = smallRatio * imgWidth;
    	var smallImgHeight = smallRatio * imgHeight;
    	$(".smallAvatarImg").width("" + smallImgWidth + "px");
    	$(".smallAvatarImg").height("" + smallImgHeight + "px");
    	$(".smallAvatarImg").css({top: "-"+smallRatio*cropBoxTop+"px", left:"-"+smallRatio*cropBoxLeft+"px"});    	
    });
});
