var total = 4;
function rndBackground(){
	var num = Math.floor(Math.random() * total);
	document.body.background = '../static/background_images/background'+ num +'.jpg';
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

function showPassword() {
	var x = document.getElementById("userInput");
	if (x.type === "password") x.type = "text";
	else x.type = "password";
}

