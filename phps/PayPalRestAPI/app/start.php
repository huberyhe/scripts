<php
require __DIR__  . '/vendor/autoload.php';
define('SITE_URL', 'http;//www.ocod.net');
$paypal = new \PayPal\Rest\ApiContext(
    new \PayPal\Auth\OAuthTokenCredential(
        'AfVInSvRmffye5_NRXYi0jQFp7J2IR6Tlqri5KPOJbpiiXhZpM_ckVloAcqkfawUJU2mp9Hb8tkhaT2F',     // ClientID
        'EHrlYIlh8xSP6RbZJih_P9sTJkIsh_GwchXZ1p-ca2wu8VFleHr_CulDmhqChvSRTejowGO-RwZ2JD0D'      // ClientSecret
    )
);