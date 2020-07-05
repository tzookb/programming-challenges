<?php


function convert($returned, $expected){
    $returned = DateTime::createFromFormat('d m Y', $returned);
    $expected = DateTime::createFromFormat('d m Y', $expected);
    if ($returned < $expected ||
        $returned->format('Y-m-d') == $expected->format('Y-m-d')
    ) {
        return 0;
    }

    if ($returned->format('Y-m') == $expected->format('Y-m')) {
        $daysDiff = (int)$returned->format('d') - (int)$expected->format('d');
        return $daysDiff*15;
    }

    if ($returned->format('Y') == $expected->format('Y')) {
        $monthsDiff = (int)$returned->format('m') - (int)$expected->format('m');
        return $monthsDiff*500;
    }

    return 10000;
}



$handle = fopen ("php://stdin","r");

$returned = trim(fgets($handle));
$expected = trim(fgets($handle));



//$returned = '2 7 1014';
//$expected = '1 1 1014';

echo convert($returned, $expected).PHP_EOL;



fclose($handle);