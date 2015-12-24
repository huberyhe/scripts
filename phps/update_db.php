<?php
require_once 'vendor/autoload.php';
$hashids = new Hashids\Hashids('this is my salt', 10, 'abcdefghij1234567890');

$db = new mysqli("localhost", "iksdbuser", "iksdb123!@#",'iksdb3');
if(mysqli_connect_errno())
{
	print 'Error connect.' . "\n";
	exit;
}
$query = 'SELECT id,username FROM iksdb3.iksuser where username REGEXP "^[0-9]+$"';
$result = $db->query($query);
$num_results = $result->num_rows;
print "There are " . $num_results . ' results.' . "\n\n";
for($i = 0; $i < $num_results; $i++)
{
	$row = $result->fetch_assoc();
	$id = $row['id'];
	$username = $row['username'];
	$username_after = $hashids->encode($username);
	
	$query = 'update iksdb3.iksuser set username = "' . $username_after . '" where id=' . $id; 
	$result_update = $db->query($query);
	$affected_rows = $db->affected_rows;
	
	printf("%5d %s %s %d %d\n", $id, $username, $username_after, $result_update, $affected_rows);
}
$result->free();
$db->close();
?>
