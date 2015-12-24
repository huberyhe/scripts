<?php
echo "Usage: " . $_SERVER["SCRIPT_NAME"] ." [strLen [strsNum]]\n\n";
if($argc < 1)
{
	echo " . Error input. Please retry!\n";
	exit();
}
$strLen = 10;
$strsNum = 10;
if(isset($argv[1])) $strLen = $argv[1];
if(isset($argv[2]) && $argv[2] < 100) $strsNum = $argv[2];

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
echo " . generating hash strings...\n";
echo str_repeat("=", $strLen + 3) . "\n";
for($i = 0; $i < $strsNum; $i ++)
{
    $salt = guid();
    $ALPHABET = "abcdefghijklmnpqrstuvwxyz123456789";
    $hashids = new Hashids\Hashids($salt, $strLen, $ALPHABET);

    $id = $hashids->encode($i);
    printf("%02d %s\n", $i + 1, $id);
    // echo $i . " " . $id . "\n";

   // $numbers = $hashids->decode($id);
   // echo $this->guid();
   // var_dump($id, $numbers);
}
echo str_repeat("=", $strLen + 3) . "\n";
echo " . generate hash strings completed.\n\n";
?>