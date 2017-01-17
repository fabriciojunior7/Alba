<?php
	session_start();
	if($nick == $nick_dados and $senha == $senha_dados){
		
		$conexao = mysqli_connect("localhost", "root", "", "alba");
		if(mysqli_connect_errno()){
			echo "Erro!";
		}
			
		$nick = $_SESSION['nick'];
			
		date_default_timezone_set("America/Bahia");
		$data = date("H:i:s - d/m/Y");
		
		$consulta_logs = "INSERT INTO logins(tipo, nick, data) VALUES('Saida', '$nick', '$data')";
		mysqli_query($conexao, $consulta_logs);
		
		
		session_destroy();
	}
	header("location:index.php");
?>