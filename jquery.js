var total = 4;
function rndBackground(){
	var num = Math.floor(Math.random() * total);
	document.body.background = '../static/background'+ num +'.jpg';
	document.body.style.backgroundRepeat = "repeat";
}

function checkpassword() {
	password = document.getElementById("password").value;
	confirmPassword = document.getElementById("confirmPassword").value;
	console.log(password);
	console.log(confirmPassword);
	if (password == confirmPassword) return true;
	else return false;
}