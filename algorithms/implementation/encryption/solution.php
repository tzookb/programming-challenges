<?php

function calc($str) {
    $size = strlen($str);
    $strArr = str_split($str);
    $sqrt = (float)sqrt($size);
    $bottom = floor($sqrt);
    $top = ceil($sqrt);

    $res = [
        'bottom-bottom' => $bottom*$bottom,
        'bottom-top' => $bottom*$top,
        'top-top' => $top*$top,
    ];

    asort($res);

    foreach ($res as $index=>$row) {
        if ($row>= $size) {
            $arrSizes = explode('-', $index);

            $rowAmount = $$arrSizes[0];
            $colAmount = $$arrSizes[1];
        }
    }

    for ($i=0 ; $i<$colAmount ; $i++) {
        $cyphedStr = '';
        $z=$i;
        while ($z<$size) {
            $cyphedStr .= $strArr[$z];
            $z = $z + $colAmount;
        }
        echo $cyphedStr.' ';
    }

}

$handle = fopen ("php://stdin","r");

$calc = trim(fgets($handle));
//$calc ='haveaniceday';
calc($calc);




fclose($handle);