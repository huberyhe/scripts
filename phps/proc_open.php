<?php
$command = '/usr/local/bin/ffmpeg -i See\ You\ Again.mp4 -y -vcodec mpeg2video -acodec mp2 -b:v 1700000 -s 640X480 -ac 2 -ab 64000 -ar 48000 -f mpegts See\ You\ Again.ts'; 
$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("file", "/tmp/error-output.txt", "a") // stderr is a file to write to
);
$cwd = '/var/www/tmp';
$env = array('some_option' => 'aeiou');
$process = proc_open($command, $descriptorspec, $pipes, $cwd, $env);

$var = proc_get_status($process);
while (intval($var['running'])) {
	$var = proc_get_status($process);
	echo time().PHP_EOL;
	sleep(2);
}

// $ppid = intval($var['pid']);
// $pids = preg_split('/\s+/', `ps -o pid --no-heading --ppid $ppid`);
// echo "ppid: $ppid".PHP_EOL;
// sleep(10);
// foreach($pids as $pid) {
//     if(is_numeric($pid)) {
//         echo "Killing $pid".PHP_EOL;
//         posix_kill($pid, 9); //9 is the SIGKILL signal
//     }
// }

fclose($pipes[0]);
fclose($pipes[1]);
proc_close($process);
// proc_close(proc_open('kill -9 '.$pid, array(), $pipes));

?>