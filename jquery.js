//var backgroundImg = ['background0.jpg','background1.jpg','background2.jpg','background3.jpg'];
//$('body').css({'background-image': 'url(../static/' + backgroundImg[Math.floor(Math.random() * backgroundImg.length)] + ')'});

var total = 4;
function rndBackground(){
	var num = Math.floor(Math.random() * total);
	document.body.background = '../static/background'+ num +'.jpg';
	document.body.style.backgroundRepeat = "repeat";
}