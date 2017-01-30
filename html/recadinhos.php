<html>
	
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="design/estilo_recadinhos.css">
		<title>Alba</title>
		<?php
			session_start();
		?>
		
	</head>
	
	<body>
	
	<?php
	
		date_default_timezone_set("America/Bahia");
		$data_agora = date("Y-m-d");
		$data_namoro = ("2015-01-10");
		$diferenca = strtotime($data_agora) - strtotime($data_namoro);
		$dias_de_namoro = floor($diferenca / (60 * 60 * 24));
		
		$nome = ucfirst($_SESSION['nick']);
	
		if(isset($_SESSION['nick']) and isset($_SESSION['senha'])){
			
			echo "
			<script src='javascript/p5.js'></script>
			<script src='javascript/p5.dom.js'></script>
			<script src='javascript/apps.js'></script>
			<script src='javascript/recadinhos.js'></script>
			
			<div id='barra_top'>
				<p id='nome_app'>Recadinhos</p><image src='design/imagens/recadinho.png' class='icones_tops' id='icone_recadinho'>
				
				
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
			
			<div id='recadinho'>
				<form method='post' action='postador.php'>
					Titulo*<br><input type='text' name='titulo' class='formulario_recadinho' id='titulo_da_postagem' /><br>
					Subtitulo<br><input type='text' name='subtitulo' class='formulario_recadinho' id='subtitulo_da_postagem' /><br><br>
					Recadinho*<br><textarea id='texto_recadinho' name='recadinho'></textarea><br><br>
					<button id='botao_postar' onclick='postar()'>Postar</button>
					<!-- <input type='submit' value='Postar' id='botao_postar' /> -->
				</form>
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