<?php
$pattern = '/time=([0-9:\.]+)\s+/';
$log_string = 'frame=10639 fps=112 q=6.4 size=  104627kB time=00:07:23.25 bitrate=1933.7kbits/s speed=4.65x';
preg_match($pattern, $log_string, $matches_array);
print_r($matches_array);

$limit_time = 30;
while($limit_time)
{
	echo get_transcoding_time('/tmp/ffreport.log').'s'.PHP_EOL;
	$limit_time--;
	sleep(1);
}


function get_transcoding_time($logfile)
{
	if(!file_exists( $logfile ) && is_readable( $logfile ) ) throw New Exception('File '.$logfile.' Not Exists or Readable.', 32);
	$log_string = get_end_line($logfile);


	$pattern = '/time=([0-9:\.]+)\s+/';
	//$log_string = 'frame=10639 fps=112 q=6.4 size=  104627kB time=00:07:23.25 bitrate=1933.7kbits/s speed=4.65x';
	if(preg_match($pattern, $log_string, $matches_array))
	{
		echo '---'.$matches_array[1].PHP_EOL;
		return ff_time_to_second($matches_array[1]);
	}
	else
		return null;
}
function get_end_line($filename)
{
	$end_line_string = '';
	$fp = fopen($filename, 'r');
	fseek($fp, -1, SEEK_END);
	while(($c = fgetc($fp)) !== false) {
		if($c == "\n" && $end_line_string) break;
		$end_line_string = $c . $end_line_string;
		fseek($fp, -2, SEEK_CUR);
	}
	fclose($fp);
	return $end_line_string;
}
function ff_time_to_second($ff_time)
{
	//00:00:02.25
	list($hour, $minute, $second) = explode(':', $ff_time);
	return $hour*60+$minute*60+$second;
}
?>
