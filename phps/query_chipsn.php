<?php
echo "Usage: " . $_SERVER["SCRIPT_NAME"] ." <usersFileName> <modelID> [inOrNot]\n\n";
if($argc < 3)
{
	echo " . Error input. Please retry!\n";
	exit();
}
if(isset($argv[1])) $usersFile = $argv[1];
if(isset($argv[2])) $modelID = intval($argv[2]);
if(isset($argv[3])) $inOrNot = intval($argv[3]);

$db = new mysqli("localhost", "root", "123456",'iksdb3');
if(mysqli_connect_errno())
{
	print 'Error connect.' . "\n";
	exit;
}
$file = fopen($usersFile, 'r');
while(! feof($file))
{
	$tmp = fgetcsv($file);
	$file_array[] = $tmp[0];
}
fclose($file);
// print_r($file_array);

for($i = 0; $i < count($file_array); $i++)
{
	$chipsn = $file_array[$i];
	$query1 = 'select * from iksdb3.iksuser where chipsn= "' . $chipsn . '"'; 
	$query2 = 'select * from iksdb3.iksuser where model_id='. $modelID .' and chipsn= "' . $chipsn . '"'; 
	$result_query1 = $db->query($query1);
	// $affected_rows = $db->affected_rows;
	$num_rows1 = $result_query1->num_rows;
	$result_query2 = $db->query($query2);
	$num_rows2 = $result_query2->num_rows;

	if(!isset($inOrNot)) printf("%s %d %d\n", $chipsn, $num_rows1, $num_rows2);
	elseif($inOrNot == $num_rows1) printf("%s %d %d\n", $chipsn, $num_rows1, $num_rows2);
}

$db->close();
?>
