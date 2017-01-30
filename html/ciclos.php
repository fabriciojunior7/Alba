<html>
	
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="design/estilo_ciclos.css">
		<title>Alba</title>
		<?php
			session_start();
		?>
		
	</head>
	
	<body>
	
	<?php
	
		date_default_timezone_set("America/Bahia");
		$data_agora = date("Y-m-d");
		
		$nome = ucfirst($_SESSION['nick']);
	
		if(isset($_SESSION['nick']) and isset($_SESSION['senha'])){
			
			echo "
			<script src='javascript/p5.js'></script>
			<script src='javascript/p5.dom.js'></script>
			<script src='javascript/apps.js'></script>
			
			<div id='barra_top'>
				<p id='nome_app'>Ciclos</p><image src='design/imagens/rosa.png' class='icones_tops' id='icone_rosa'>
				
				
				<button id='botao_apps' onclick='abrir_apps()'>Apps</button>
				<div id='barra_apps'>
					<a href='index.php'><image src='design/imagens/mobile.png' class='icones_apps' id='icone_mobile'></a>
					<a href='ciclos.php'><image src='design/imagens/rosa.png' class='icones_apps' id='icone_rosa'></a>
					<a href='recadinhos.php'><image src='design/imagens/recadinho.png' class='icones_apps' id='icone_recadinho'></a>
					<a href=''><image src='design/imagens/breve2.png' class='icones_apps'></a>
					<a href=''><image src='design/imagens/breve2.png' class='icones_apps'></a>
					<a href=''><image src='design/imagens/breve2.png' class='icones_apps'></a>
					<a href=''><image src='design/imagens/breve2.png' class='icones_apps'></a>
					<a href=''><image src='design/imagens/breve2.png' class='icones_apps'></a>
					<a href='logins.php'><image src='design/imagens/chave.png' class='icones_apps' id='icone_chave'></a>
				</div>
				<a href='destruidor.php'><button id='botao_sair'>Sair</button></a>
			</div>
			
			<div class='postagem' id='calendario'>
				Próximo Ciclo: 06/02/2017
			</div>
			
			<div class='postagem' id='hoje'>
				
			</div>
			
			<div class='postagem' id='estatisticas'>
				
			</div>
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			";
		}
		else{
			header("location:index.php");
		}
	
	?>
	
	<!--<br><br><br><br><br><br><br><br><br><br><br><br><h1>Postagens!</h1>-->
	
	
	</body>
	
</html>