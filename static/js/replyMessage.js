$(document).ready(function(){
        $(".replyMessageForm").submit(function(){
            var targetid = $(this).attr("targetid");
            var masterCommentid = $(this).attr("masterCommentid");
            var content = $(this).find("textarea").first().val();
            $(this).ajaxSubmit({
                dataType: "json",
                headers: { "X-CSRFToken": $.cookie("csrftoken") },
                type: "POST",
                url: "/njuG/sendMessage/",
                data: {"targetid": targetid, "messageContent": content},
                success: function(response){
                    showMessage(1,"回复成功！");
                }
            });
            return false;
        });
});
