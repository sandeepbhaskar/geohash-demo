<?php
	$howfar = $_REQUEST['howfar'];
	if ($howfar == '1')
		$redirect = "index.html";
	else
		$redirect = "d".$howfar.".html";
	header("Location: $redirect");
?>

