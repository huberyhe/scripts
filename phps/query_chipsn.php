<?php
$db = new mysqli("localhost", "root", "123456",'iksdb3');
if(mysqli_connect_errno())
{
	print 'Error connect.' . "\n";
	exit;
}

$file = fopen('users.txt', 'r');
while(! feof($file))
{
	$file_array[] = fgetcsv($file)[0];
}
fclose($file);
// print_r($file_array);

for($i = 0; $i < count($file_array); $i++)
{
	$chipsn = $file_array[$i];
	$query = 'select * from iksdb3.iksuser where model_id=15 and chipsn= "' . $chipsn . '"'; 
	$reult_query = $db->query($query);
	// $affected_rows = $db->affected_rows;
	$num_rows = $reult_query->num_rows;
	if(!$num_rows) printf("%s %d\n", $chipsn, $num_rows);
}

$db->close();
?>
