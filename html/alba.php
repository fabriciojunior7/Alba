<html>
	
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="estilo_alba.css">
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
			
			if($_SESSION['nick'] == "junior"){
				$cor = "#009933";
			}
			else if($_SESSION['nick'] == "debora"){
				$cor = "#ff0066";
			}
			
			echo "
			
			<div id='barra_top'>
				<p id='nome'><font color=$cor>$nome</font></p>
				
				<image src='imagens/coracao.png' id='coracao1'>
				<p id='dias_de_namoro'>$dias_de_namoro Dias</p>
				<image src='imagens/coracao.png' id='coracao2'>
				
				<a href='destruidor.php'><input type='submit' value='Sair' id='botao_sair'></a>
			</div>
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			";
		}
		else{
			header("location:index.php");
		}
	
	?>
	
	</body>
	
</html>