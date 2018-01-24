<?php
ini_set('display_errors',1);            //错误信息
ini_set('display_startup_errors',1);    //php启动错误信息
error_reporting(-1);                    //打印出所有的 错误信息

if('cli' === php_sapi_name())
{
	define('BS', "\n");
	cli_set_process_title('test.php');
}
else
	define('BS', "<br />");

function blockEnd($is_exit=false)
{
	if (!$is_exit)
		echo BS. '-------------------------------'. BS;
	else
	{
		echo BS. '-------------------------------';
		exit();
	}
}

function debug($var_str)
{
	$trace =debug_backtrace();
	if(empty($trace)) return;
	$trace_last = $trace[count($trace) - 1];
	echo $trace_last['file']. ': '. $trace_last['line']. BS;
	if (isset($var_str)) {
		var_dump($var_str);
	} else {
		echo $var_str;
	}
}