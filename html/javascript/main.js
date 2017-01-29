var ver;

function setup(){
	ver = false;
}

function draw(){
	
}

function abrir_apps(){
	if(ver == false){
		ver = true;
		select("#barra_apps").style("display", "block");
	}
	else if(ver == true){
		ver = false;
		select("#barra_apps").style("display", "none");
	}
	print(ver);
}