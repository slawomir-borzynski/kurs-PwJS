function checkForm(){
	
	var err=false;
	var errText="";
	var contactName = document.getElementById("nazwa");
	var contactEmail = document.getElementById("e-mail");
	var contactText = document.getElementById("wiadomosc");
	
	if(contactName.value == "") {document.getElementById("errorNazwa").className="alert alertdanger";  err=true;}
	if(contactEmail.value == "") {document.getElementById("errorMail").className="alert alertdanger";  err=true;}
	else{
		var email = contactEmail.value;
		var regex = /^[a-zA-Z0-9._-]+@([a-zA-Z0-9.-]+\.)+[a-zA-Z0-9.-]{2,4}$/;
		if(regex.test(email)==false)
		{
			document.getElementById("errorFormat").className="alert alertdanger"; 
			error=true;
	} }
	if(contactText.value == "") {document.getElementById("errorWiadomosc").className="alert alertdanger";  err=true;}
	
	if(!err) return true;
	else return false;

}