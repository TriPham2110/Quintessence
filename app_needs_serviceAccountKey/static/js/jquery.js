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

function uploadMsg(){

	var input = document.getElementById('file');

	for (var i=0; i<input.files.length; i++){
		var ext= input.files[i].name.substring(input.files[i].name.lastIndexOf('.')+1).toLowerCase();

		if ((ext == 'jpg') || (ext == 'png')){
			$("#msg").text("Files are supported")
		}
		else{
			$("#msg").text("Files are NOT supported")
			document.getElementById("file").value ="";
		}
	}
}

function uploadFirebase() {
	// Initialize Firebase
	var config = {
		"apiKey": "",
		"authDomain": ".firebaseapp.com",
		"databaseURL": ".firebaseio.com",
		"projectId": "",
		"storageBucket": ".appspot.com",
		"messagingSenderId": ""
	};
	firebase.initializeApp(config);
	//-------------------------------------

	var uploader = document.getElementById('upload-button');
	var fileButton = document.getElementById('file');
	fileButton.addEventListener('change', function(e){
	var file = e.target.files[0];
	var storageRef = firebase.storage().ref('gallery/'+file.name);
	var task = storageRef.put(file);
	task.on('state_changed', function progress(snapshot) {
		var percentage = (snapshot.bytesTransferred/snapshot.totalBytes)*100;
		uploader.value = percentage;

	  }, function error(err) {


	  },function complete() {
			var postKey = firebase.database().ref('images/').push().key;
			var downloadURL = task.snapshot.downloadURL;
			var updates = {};
			var postData = {
				url: downloadURL,
				name: file.name
			}
			updates['/images/'+postKey]=postData;
			firebase.database().ref().update(updates);
	  });
	});  
}
