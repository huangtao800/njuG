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
                    showMessage(1,"回复成功！");
                }
            });
            return false;
        });
});