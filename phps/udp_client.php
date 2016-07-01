<?php
$fp = stream_socket_client("udp://127.0.0.1:9999", $errno, $errstr);
if (!$fp) {
    echo "ERROR: $errno - $errstr<br />\n";
} else {
    fwrite($fp, "hello\n");
    echo fread($fp, 26);
    fclose($fp);
}
?> 