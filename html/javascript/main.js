var frames = 100;
var cor = 255;

function setup(){
	//paragrafo = createP(cor);
	saida = createElement("h1", "");
	entrada = createInput("");
}

function draw(){
	frameRate(frames);
	//paragrafo.html(mouseX + " " + mouseY);
	saida.html(responder());
}

function responder(){
	if(entrada.value() == "oi"){
		return("Boa Noite!!");
	}
	else{
		return(":-)");
	}
}









