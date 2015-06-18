$(document).ready(function(){
	$("#postForm").submit(function(){
		$(this).ajaxSubmit({
			dataType: "json",
			headers: { "X-CSRFToken": $.cookie("csrftoken") },
			type: 'POST',
			contentType: "application/json; charset=utf-8",
			success: function(response){
				alert("hello");
				
				alert(response["result"]);
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
