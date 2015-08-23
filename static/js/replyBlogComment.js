$(document).ready(function(){
        $(".replyCommentForm").submit(function(){
            var blogid = $(this).attr("blogid");
            var commentid = $(this).attr("commentid");
            var masterCommentid = $(this).attr("masterCommentid");
            var content = $(this).find("textarea").first().val();
            $(this).ajaxSubmit({
                dataType: "json",
                headers: { "X-CSRFToken": $.cookie("csrftoken") },
                type: "POST",
                url: "/njuG/replyBlogComment/",
                data: {"blogid": blogid, "commentid": commentid, "content": content, "masterCommentid":masterCommentid},
                success: function(response){
                	result = response['result'];
                	if(result){
                		showMessage(1,"回复成功！");
                		location.reload();
                	}else{
						if(response["msg"]==="user not login"){
							var url = window.location.protocol+"//"
								+window.location.host+"/accounts/login";
							window.location = url;
						}
                	}
                }
            });
            return false;
        });
});
