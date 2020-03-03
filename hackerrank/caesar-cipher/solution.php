<?php

function convert($string, $cipher){
    $az = range('a', 'z');
    $azValIndex = array_flip($az);

    $cipher = $cipher % sizeof($az);
    $isBig = false;

    $string = str_split($string);

    foreach ($string as $i=>$char) {
        if ( ! ctype_alpha($char)) {
            continue;
        }

        if (ctype_upper($char)) {
            $isBig = true;
            $char = mb_strtolower($char);
        }

        $charVal = $azValIndex[$char];
        $charVal = $charVal+$cipher;
        $charVal = $charVal % sizeof($az);

        $char = $az[$charVal];

        if ($isBig) {
            $char = mb_strtoupper($char);
        }

        $string[$i] = $char;

        $isBig = false;
    }
    return implode('', $string);
}



$handle = fopen ("php://stdin","r");

$size = trim(fgets($handle));
$string = trim(fgets($handle));
$cipher = trim(fgets($handle));

if(0) {
    $size = 11;
    $string = 'middle-Outz';
    $cipher = 2;
}

//$returned = '2 7 1014';
//$expected = '1 1 1014';

echo convert($string, $cipher).PHP_EOL;
//echo 'okffng-Qwvb'.PHP_EOL;


fclose($handle);