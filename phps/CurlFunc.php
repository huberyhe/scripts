<?php
class CurlFunc{
    function curlCommon($URL,$type,$params,$headers){
        $ch = curl_init($URL);
        $timeout = 5;
//        curl_setopt ($ch, CURLOPT_URL, $URL);
        if($headers != ""){
            curl_setopt ($ch, CURLOPT_HTTPHEADER, $headers);
        }else {
//            curl_setopt($ch, CURLOPT_HEADER, 0);
            curl_setopt ($ch, CURLOPT_HTTPHEADER, array(
                'Content-type: application/json',
                'Content-Length: ' . strlen($params))
            );
        }
        curl_setopt ($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
        switch ($type){
            case "GET" :
                curl_setopt($ch, CURLOPT_HTTPGET, true);
                break;
            case "POST":
                curl_setopt($ch, CURLOPT_POST, true);
                curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
//                echo 'params=' . $params . '<br>';
                break;
            case "PUT" :
                curl_setopt ($ch, CURLOPT_CUSTOMREQUEST, "PUT");
                curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
                break;
            case "DELETE":
                curl_setopt ($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
                curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
                break;
        }
        $file_contents = curl_exec($ch);//获得返回值
        curl_close($ch);
        return $file_contents;
    }
}

?>