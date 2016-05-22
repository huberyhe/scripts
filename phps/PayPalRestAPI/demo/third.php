<?php
// 1. Autoload the SDK Package. This will include all the files and classes to your autoloader
require __DIR__  . '/vendor/autoload.php';

// 2. Define PP_CONFIG_PATH directory
if(!defined("PP_CONFIG_PATH")) {
define("PP_CONFIG_PATH", __DIR__);
}

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
//ApiContext is not required anymore as it get loaded from file
$creditCard->create();
echo $creditCard;
}
catch (\PayPal\Exception\PayPalConnectionException $ex) {
echo $ex;
}