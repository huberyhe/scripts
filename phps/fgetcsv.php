<?php
    $file = fopen('channels.txt', 'r');
    while(! feof($file))
	{    
		$file_array[] = fgetcsv($file);
	}
    print_r($file_array);
	$s_array = array('aaa', 'bbb', 'ccc', 123, '1234');
	print_r($s_array);
	foreach($s_array as $value)
	{
		if(is_numeric($value)) print $value . "\n";
	}

?>
