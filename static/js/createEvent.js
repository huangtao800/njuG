$(document).ready(function(){
	$("#postForm").submit(function(){
		var imgPkList = new Array();
		$.each($("button.delete"), function(){
			imgPkList.push($(this).attr("data-imgpk"));
		});
		$(this).ajaxSubmit({
			dataType: "json",
			headers: { "X-CSRFToken": $.cookie("csrftoken") },
			type: 'POST',
			data: {"content": $("#postArea").val(), "imgPkList[]": imgPkList},
			success: function(response){
				var result = response['result'];
				if(result==1){
					$("#postForm textarea").val('');
					$("#imgPreviewTable").empty();
					showMessage(1, "发布成功！");
				}
				else{
					if(response["msg"]==="user not login"){
						var url = window.location.protocol+"//"
							+window.location.host+"/accounts/login";
						window.location = url;
					}
				}
			},
			error: function(xhr, ajaxOptions, thrownError){
				
			}
		});
		return false;
	});
	
	
	$(".commentForm").submit(function(){
		var commentContent = $(this).find("input").first();
		var postid = $(this).find("button").first().attr("postid");
		$(this).ajaxSubmit({
			url: "/njuG/postComment",
			dataType:"json",
			headers: { "X-CSRFToken": $.cookie("csrftoken") },
			type: "POST",
			data: {"content": commentContent.val(), "postid":postid},
			success: function(response){
				result=response['result'];
				if(result==1){
					commentContent.val('');
					showMessage(1,"评论成功！");
				}else{
					if(response["msg"]==="user not login"){
						var url = window.location.protocol+"//"
							+window.location.host+"/accounts/login";
						window.location = url;
					}
				}
			},		
		});
		return false;
	});

	$(".like").click(function(){
		var postid = $(this).attr("postid");
		var like = $(this);
		if(!postid===parseInt(postid, 10))	return;
		if(like.children("i").first().hasClass("liked")){
			$.ajax({
				url: "/njuG/notLikePost",
				dataType: "json",
				headers: { "X-CSRFToken": $.cookie("csrftoken") },
				type: 'POST',
				data: {"postid": postid},
				success: function(response){
					var result = response['result'];
					if(result==1){
						var likeCount = like.children("i.likeCount").first();
						likeCount.html(parseInt(likeCount.text())-1);
						like.children("i").first().removeClass("liked");
					}else{
						if(response["msg"]==="user not login"){
							var url = window.location.protocol+"//"
								+window.location.host+"/accounts/login";
							window.location = url;
						}
			}
				},
			});
		}else{
			$.ajax({
				url: "/njuG/likePost",
				dataType: "json",
				headers: { "X-CSRFToken": $.cookie("csrftoken") },
				type: 'POST',
				data: {"postid": postid},
				success: function(response){
					var result = response['result'];
					if(result==1){
						var likeCount = like.children("i.likeCount").first();
						likeCount.html(parseInt(likeCount.text())+1);
						like.children("i").first().addClass("liked");
					}else{
						if(response["msg"]==="user not login"){
							var url = window.location.protocol+"//"
								+window.location.host+"/accounts/login";
							window.location = url;
						}
			}
				},
			});				
		}
	});
	
});
