$(document).ready(function(){
	$("#postForm").submit(function(){
		$(this).ajaxSubmit({
			dataType: "json",
			headers: { "X-CSRFToken": $.cookie("csrftoken") },
			type: 'POST',
			contentType: "application/json; charset=utf-8",
			success: function(response){
				var result = response['result'];
				if(result==1){}
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
