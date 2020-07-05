<?php

function calc($cycles) {
    $height = 1;
    $fullCycles = floor($cycles/2);
    $half = $cycles%2;

    for ($i=0 ; $i<$fullCycles ; $i++) {
        $height *= 2;
        $height += 1;
    }

    if ($half)
        $height *= 2;

    return $height;
}

$handle = fopen ("php://stdin","r");

$treeAmount = trim(fgets($handle));
$i = 0;

while ($i++ < $treeAmount) {
    $treeCycles = trim(fgets($handle));
    echo calc($treeCycles).PHP_EOL;
}

//echo calc(3).PHP_EOL;

fclose($handle);