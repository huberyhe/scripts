<?php
require __DIR__ . '/vendor/autoload.php';

$apiContext = new \PayPal\Rest\ApiContext(
    new \PayPal\Auth\OAuthTokenCredential(
        'AfVInSvRmffye5_NRXYi0jQFp7J2IR6Tlqri5KPOJbpiiXhZpM_ckVloAcqkfawUJU2mp9Hb8tkhaT2F',     // ClientID
        'EHrlYIlh8xSP6RbZJih_P9sTJkIsh_GwchXZ1p-ca2wu8VFleHr_CulDmhqChvSRTejowGO-RwZ2JD0D'      // ClientSecret
    )
);

$creditCard = new \PayPal\Api\CreditCard();
$creditCard->setType("visa")
    ->setNumber("4417119669820331")
    ->setExpireMonth("11")
    ->setExpireYear("2019")
    ->setCvv2("012")
    ->setFirstName("Joe")
    ->setLastName("Shopper");

try {
    $creditCard->create($apiContext);
    echo $creditCard;
}
catch (\PayPal\Exception\PayPalConnectionException $ex) {
    // This will print the detailed information on the exception. 
    //REALLY HELPFUL FOR DEBUGGING
    echo $ex->getData();
}