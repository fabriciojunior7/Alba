<?php
	session_start();
	
	date_default_timezone_set("America/Bahia");
	$data_agora = date("d/m/Y - H:i:s");
	
	if(isset($_SESSION['nick']) and isset($_SESSION['senha'])){
		
		$conexao = mysqli_connect("localhost", "root", "", "alba");
		mysqli_query($conexao, "SET NAMES 'utf8'");
		if(mysqli_connect_errno()){
			echo "Erro!";
		}
		
		$nome = $_SESSION['nick'];
		$titulo = $_POST['titulo'];
		$subtitulo = $_POST['subtitulo'];
		$recadinho = $_POST['recadinho'];
		
		if($titulo != "" && $recadinho != ""){
			$inserir = "INSERT INTO postagens (tipo, nick, titulo, subtitulo, legenda, data) VALUES ('recadinho', '$nome', '$titulo', '$subtitulo', '$recadinho', '$data_agora')";
			if(mysqli_query($conexao, $inserir)){
				echo "<h1>Postado!</h1>";
				mysqli_close($conexao);
				header("refresh:1; url=index.php");
			}
		}
		
		else{
			echo "Postagem em branco...";
			header("refresh:3; url=recadinhos.php");
		}
		
		
		
	}
		
	else{
		header("location:index.php");
	}





?>