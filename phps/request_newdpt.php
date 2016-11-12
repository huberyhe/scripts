<?php
$strLen = 16;
$strsNum = 10100;

include("vendor/autoload.php");
function guid(){
    if (function_exists('com_create_guid')){
        return com_create_guid();
    }else{
        mt_srand((double)microtime()*10000);//optional for php 4.2.0 and up.
        $charid = strtoupper(md5(uniqid(rand(), true)));
        $hyphen = chr(45);// "-"
        $uuid = chr(123)// "{"
            .substr($charid, 0, 8).$hyphen
            .substr($charid, 8, 4).$hyphen
            .substr($charid,12, 4).$hyphen
            .substr($charid,16, 4).$hyphen
            .substr($charid,20,12)
            .chr(125);// "}"
        return $uuid;
    }
}

for($i = 0; $i < $strsNum; $i ++)
{
    $salt = guid();
    $ALPHABET = "abcdefghijklmnpqrstuvwxyz123456789";
    $hashids = new Hashids\Hashids($salt, $strLen, $ALPHABET);

    $id = $hashids->encode($i);
    // echo $i . " " . $id . "\n";

    $url = "http://103.238.227.41/newdpt/request.php?orderNo=TEST1600&chipId=".$id."&request=uniqueOtp";
    // printf("url:".$url."\n");

	//初始化
	$ch = curl_init();

    //设置选项，包括URL
	curl_setopt($ch, CURLOPT_URL, $url);

	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_HEADER, 0);


	//执行并获取HTML文档内容
	$output = curl_exec($ch);

	//打印获得的数据
    printf("%05d %s %03d %s".PHP_EOL, $i + 1, $id, strlen($output), $url);

	//释放curl句柄
	curl_close($ch);

   // $numbers = $hashids->decode($id);
   // echo $this->guid();
   // var_dump($id, $numbers);
}




