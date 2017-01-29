<!--
Fabricio Vidal da Costa Junior
Inicio: 16/01/2017
-->

<html>

	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="design/estilo_index.css">
		<title>Alba</title>
		<?php
			session_start();
			if(isset($_SESSION['nick']) and isset($_SESSION['senha'])){
				header("location:alba.php");
			}
		?>
	</head>
	
	<body>
	
	<div id="plano-de-fundo"></div>
	
	<div id="caixa">
		<br>
		<form action="conector.php" method="post">
			Nome<br><input name="nick" type="text" class="input-texto" /><br>
			Senha<br><input name="senha" type="password" class="input-texto" />
			<br><br><input value="Entrar" type="submit" class="input-botao" />
		</form>
	</div>
	
	
	</body>
	
</html>
		