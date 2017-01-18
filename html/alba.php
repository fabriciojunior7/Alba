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
	
		function diffDate($d1, $d2, $type='', $sep='-'){
			$d1 = explode($sep, $d1);
			$d2 = explode($sep, $d2);
			switch ($type){
				case 'A':
				$X = 31536000;
				break;
				case 'M':
				$X = 2592000;
				break;
				case 'D':
				$X = 86400;
				break;
				case 'H':
				$X = 3600;
				break;
				case 'MI':
				$X = 60;
				break;
				default:
				$X = 1;
			}
			return floor( ( ( mktime(0, 0, 0, $d2[1], $d2[2], $d2[0]) - mktime(0, 0, 0, $d1[1], $d1[2], $d1[0] ) ) / $X ) );
		}
	
	
	
		date_default_timezone_set("America/Bahia");
		$data = date("Y-m-d");
		$data_namoro = ("2015-01-10");
		
		$dias_de_namoro = diffDate($data_namoro, $data, "D");
		
		$nome = ucfirst($_SESSION['nick']);
	
		if(isset($_SESSION['nick']) and isset($_SESSION['senha'])){
			echo "
			
			<div id='barra_top'>
				<p id='nome'>$nome</p>
				
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