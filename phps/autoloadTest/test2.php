<?php
require_once('vendor/autoload.php');

$cf = new \Core\CurlFunc();
$cf->setTimeout(10);
echo $cf->curlCommon('http://localhost');
blockEnd();
