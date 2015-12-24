<?php
$db = new mysqli("localhost", "iksdbuser", "iksdb123!@#",'iksdb3');
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
print_r($file_array);

$query = 'select * from iksdb3.iksuser where model_id=2';
$result = $db->query($query);
$num_results = $result->num_rows;
print "There are " . $num_results . ' results.' . "\n\n";

for($i = 0; $i < count($file_array); $i++)
{
	$chipsn = $file_array[$i];
	$query = 'delete from iksdb3.iksuser where chipsn= "' . $chipsn . '"'; 
	$result_update = $db->query($query);
	$affected_rows = $db->affected_rows;
	printf("%s %d %d\n", $chipsn, $result_update, $affected_rows);
}

// for($i = 0; $i < $num_results; $i++)
// {
// 	$row = $result->fetch_assoc();
// 	$id = $row['id'];
// 	$username = $row['username'];
// 	$username_after = $hashids->encode($username);
	
// 	$query = 'update iksdb3.iksuser set username = "' . $username_after . '" where id=' . $id; 
// 	$result_update = $db->query($query);
// 	$affected_rows = $db->affected_rows;
	
// 	printf("%5d %s %s %d %d\n", $id, $username, $username_after, $result_update, $affected_rows);
// }
// $result->free();
$db->close();
?>
