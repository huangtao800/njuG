function validateSchool(){
	var onlyForSchool = $("#id_onlyForSchool").prop("checked");
	var openToAll = $("#openToAll").prop("checked");
	var schoolList = [];
    $.each($("#id_openSchoolList option:selected"),function(){
        schoolList.push($(this).val());
    });
    if(!onlyForSchool && !openToAll){
    	if(schoolList.length==0){
    		return false;
    	}
    }
    return true;
}

function validateContact(){
	var contact = $("#id_contact").val();
	var detailContact = $("#id_detailContact").val();
	if(contact=="微信" && !detailContact){
		return false;
	}
	return true;
}

$(document).ready(function(){
	$("#createActivityForm").submit(function(){
		if(!validateSchool()){
			$("#error_message").text("请选择活动范围");
		}
		if(!validateContact()){
			$("#error_message").text("请填写微信号，或选择其他联系方式");
		}
		return false;
	});
});
