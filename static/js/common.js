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