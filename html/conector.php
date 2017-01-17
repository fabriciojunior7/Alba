<html>

	<head>
		<meta charset="utf-8">
		<title>Alba</title>
		<?php
			$conexao = mysqli_connect("localhost", "root", "", "alba");
			if(mysqli_connect_errno()){
				echo "Erro!";
			}
			
			$nick = $_POST['nick'];
			$senha = $_POST['senha'];
			
			date_default_timezone_set("America/Bahia");
			$data = date("H:i:s - d/m/Y");
			
			$consulta = "SELECT nick, senha FROM usuarios";
			$dados = mysqli_query($conexao, $consulta);
			
			while($saida = mysqli_fetch_array($dados)){
				$nick_dados = $saida['nick'];
				$senha_dados = $saida['senha'];
				
				if($nick == $nick_dados and $senha == $senha_dados){
					session_start();
					$_SESSION['nick'] = $nick;
					$_SESSION['senha'] = $senha;
					
					$consulta_logs = "INSERT INTO logins(tipo, nick, data) VALUES('Entrada', '$nick', '$data')";
					mysqli_query($conexao, $consulta_logs);
					
					header("location:alba.php");
					break;
				}

			}
			
			mysqli_close($conexao);
			
			if(!isset($_SESSION['nick'])){
				echo "<center><h2>Nome ou senha incorretos...</h2></center>";
				header("refresh:3; url=index.php");
			}
			
			
		?>
	</head>
	
	<body>
	
	</body>
	
</html>
	