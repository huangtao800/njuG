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
	
	$('#postButton').click(function(){
		$("#postForm").submit();
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
