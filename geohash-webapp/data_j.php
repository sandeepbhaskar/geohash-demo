<?php
	$howfar = $_REQUEST['howfar'];
	$url = 'http://ideophone.net/services/earthcalling/mvp/getNearbyPlace?data={"howfar":"'.$howfar.'","place_id":"2"}';
	$data = json_decode(file_get_contents($url));
	$output = Array();
	$output['results'] = count($data->response);
	$output['response'] = Array();
	$output['response'] = $data->response;
	echo json_encode($output);
?>

