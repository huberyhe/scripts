<?php
namespace Core;

class CurlFunc{
    const CT_GET = 'get';
    const CT_POST = 'post';
    const CT_PUT = 'put';
    const CT_DELETE = 'delete';
   
    private $timeout = 5;
    public function setTimeout($timeout) {
        $this->timeout = $timeout;
    }
    public function curlCommon($URL, $type='get', $params=null, $headers=null){

        $ch = curl_init($URL);
        //curl_setopt($ch, CURLOPT_URL, $URL);
        if (!empty($headers)) {
            curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        } else {
            //curl_setopt($ch, CURLOPT_HEADER, 0);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array(
                'Content-type: application/json',
                'Content-Length: '. strlen($params))
            );
        }
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $this->timeout);
        switch ($type) {
            case self::CT_GET:
                curl_setopt($ch, CURLOPT_HTTPGET, true);
                break;
            case self::CT_POST:
                curl_setopt($ch, CURLOPT_POST, true);
                curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
                break;
            case self::CT_PUT:
                curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");
                curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
                break;
            case self::CT_DELETE:
                curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
                curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
                break;
            default:
                break;
        }
        $file_contents = curl_exec($ch);//获得返回值
        curl_close($ch);

        return $file_contents;
    }
}

?>
