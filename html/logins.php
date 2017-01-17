<html>

	<head>
		<meta charset="utf-8">
		<title>Alba - Logins</title>
		<?php
			session_start();
		?>
	</head>
	
	<body>
	
		<?php
			
			if(isset($_SESSION['nick']) and isset($_SESSION['senha'])){
				
				$conexao = mysqli_connect("localhost", "root", "", "alba");
				if(mysqli_connect_errno()){
					echo "Erro!";
				}
				
				$consulta_logs = "SELECT tipo, nick, data FROM logins ORDER BY id DESC";
				$dados = mysqli_query($conexao, $consulta_logs);
			
				while($saida = mysqli_fetch_array($dados)){
					echo "<h4>$saida[nick], $saida[tipo] - ($saida[data])</h4>";
				}
				
			}
			else{
				header("location:index.php");
			}
	
		?>
	
	</body>
	
</html>