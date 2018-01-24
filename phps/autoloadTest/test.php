<?php
function __autoload($name)
{
    $class_path = str_replace('\\', DIRECTORY_SEPARATOR, $name);
    $file = realpath(__DIR__). '/'. $class_path. '.php';
    if (file_exists($file)) {
        require_once($file);
        if (class_exists($name, false)) {
            return true;
        } else {
            return false;
        }
        return false;
    }
}

echo MyClass\MyClass::getNamespace();

new \Core\CurlFunc();
