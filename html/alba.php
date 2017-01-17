<html>
	
	<head>
		<meta charset="utf-8">
		<title>Alba</title>
		<?php
			session_start();
		?>
	</head>
	
	<body>
	
	<?php
	
		date_default_timezone_set("America/Bahia");
		$data = date("H:i:s - d/m/Y");
	
		if(isset($_SESSION['nick']) and isset($_SESSION['senha'])){
			echo "<center><h1>ONLINE";
			echo "<br><a href='destruidor.php'>Sair</a></h1></center>";
			echo "<br><br><br><center>Eu amo o meu bebe...</center>";
		}
		else{
			header("location:index.php");
		}
	
	?>
	
	</body>
	
</html>