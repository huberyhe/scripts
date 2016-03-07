<?php
// 1. Autoload the SDK Package. This will include all the files and classes to your autoloader
// Used for composer based installation
require __DIR__  . '/vendor/autoload.php';
// Use below for direct download installation
// require __DIR__  . '/PayPal-PHP-SDK/autoload.php';

// After Step 1
$apiContext = new \PayPal\Rest\ApiContext(
    new \PayPal\Auth\OAuthTokenCredential(
        'AfVInSvRmffye5_NRXYi0jQFp7J2IR6Tlqri5KPOJbpiiXhZpM_ckVloAcqkfawUJU2mp9Hb8tkhaT2F',     // ClientID
        'EHrlYIlh8xSP6RbZJih_P9sTJkIsh_GwchXZ1p-ca2wu8VFleHr_CulDmhqChvSRTejowGO-RwZ2JD0D'      // ClientSecret
    )
);

// After Step 2
$creditCard = new \PayPal\Api\CreditCard();
$creditCard->setType("visa")
    ->setNumber("4417119669820331")
    ->setExpireMonth("11")
    ->setExpireYear("2019")
    ->setCvv2("012")
    ->setFirstName("Joe")
    ->setLastName("Shopper");

// After Step 3
try {
    $creditCard->create($apiContext);
    echo $creditCard;
}
catch (\PayPal\Exception\PayPalConnectionException $ex) {
    // This will print the detailed information on the exception. 
    //REALLY HELPFUL FOR DEBUGGING
    echo $ex->getData();
}