$(document).ready(function(){
	$("#postForm").submit(function(){
		$(this).ajaxSubmit({
			dataType: "json",
			headers: { "X-CSRFToken": $.cookie("csrftoken") },
			type: 'POST',
			data: {"content": $("#postArea").val()},
			success: function(response){
				var result = response['result'];
				if(result==1){
					$("#postForm textarea").val('');
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

function showMessage(success, content){
	if(success==1){
		var infoDiv = $("#postSuccess");
		if(!infoDiv.length){
			infoDiv = $(document.createElement("div"));
			infoDiv.addClass("ui positive message message");
			var p = $(document.createElement("p"));
			p.append(content);
			infoDiv.append(p);
			infoDiv.hide();
			infoDiv.appendTo("body");
		}
		infoDiv.transition('fade');
		setTimeout(function(){
			infoDiv.transition('fade');
		},2000);
	}
}
