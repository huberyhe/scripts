<?php
require_once("CurlFunc.php");
$max_req = 100;
$url = "http://iksdbrr.noip.us:16000/api/v1.0";
$curlFunc = new CurlFunc();
$num_s1 = $num_s2 = 0;
$s1_ip = '184.168.221.77';
$s2_ip = '46.166.129.214';
for($i = 0; $i < $max_req; $i++)
{
	$resultJson = $curlFunc->curlCommon($url,"get","","");
	$resultArray = json_decode($resultJson, true);
	$local_ip = $resultArray['local'];
	printf("%d %s\n", $i, $local_ip);
	if($local_ip == $s1_ip) $num_s1++;
	elseif ($local_ip == $s2_ip) $num_s2++;
	else var_dump($resultArray);
}
printf("%s: %d\n", $s1_ip, $num_s1);
printf("%s: %d\n", $s2_ip, $num_s2);

?>
