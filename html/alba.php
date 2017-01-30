<html>
	
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="design/estilo_alba.css">
		<title>Alba</title>
		<?php
			session_start();
		?>
		
	</head>
	
	<body>
	
	<?php
	
		date_default_timezone_set("America/Bahia");
			$data_agora = date("H:i:s - d/m/Y");
		
		$nome = ucfirst($_SESSION['nick']);
	
		if(isset($_SESSION['nick']) and isset($_SESSION['senha'])){
			
			if($_SESSION['nick'] == "junior"){
				$cor = "#009933";
			}
			else if($_SESSION['nick'] == "debora"){
				$cor = "#ff0000";
			}
			
			echo "
			<script src='javascript/p5.js'></script>
			<script src='javascript/p5.dom.js'></script>
			<script src='javascript/apps.js'></script>
			
			<div id='barra_top'>
				<p id='nome'><font color=$cor>$nome</font></p>
				
				
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
			</div>";
			
			$conexao = mysqli_connect("localhost", "root", "", "alba");
			mysqli_query($conexao, "SET NAMES 'utf8'");
			if(mysqli_connect_errno()){
				echo "Erro!";
			}
			
			$consulta = "SELECT * FROM postagens ORDER BY id DESC";
			$dados = mysqli_query($conexao, $consulta);
			
			while($saida = mysqli_fetch_array($dados)){
				$tipo_postagem = $saida['tipo'];
				$nick_postagem = $saida['nick'];
				$titulo_postagem = $saida['titulo'];
				$subtitulo_postagem = $saida['subtitulo'];
				$legenda_postagem = $saida['legenda'];
				$link_postagem = $saida['link'];
				$data_postagem = $saida['data'];
				$data_postagem = substr($data_postagem, 0, 18);
				
				echo "<div id='postagens'>";
				
				if($tipo_postagem == "recadinho"){
					if($titulo_postagem != ""){
						if($nick_postagem == "junior"){
							$cor = "#009933";
						}
						else if($nick_postagem = "debora"){
							$cor = "#ff0000"; 
						}
						echo "<p id='titulo_postagem'><font color=$cor>$titulo_postagem</font></p>";
					}
					if($subtitulo_postagem != ""){
						echo "<p id='subtitulo_postagem'>$subtitulo_postagem</p>";
					}
					else{
						echo "<br>";
					}
					
					if($titulo_postagem != "" or $subtitulo_postagem != ""){
						echo "<hr id='separador_postagem'>";
					}
					if($legenda_postagem != ""){
						echo "<p id='legenda_postagem'>$legenda_postagem</p>";
					}
					if($data_postagem != ""){
						echo "<p id='data_postagem'>$data_postagem</p>";
					}
					
				}
				
				echo "</div>";
			}
			
			echo "<br><br><br><br><br><br><br><br><br><br><br>";
			mysqli_close($conexao);
			
		}
		else{
			header("location:index.php");
		}
	
	?>
	
	<!--<br><br><br><br><br><br><br><br><br><br><br><br><h1>Postagens!</h1>-->
	
	
	</body>
	
</html>