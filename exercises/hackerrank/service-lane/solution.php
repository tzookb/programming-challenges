<?php

use Illuminate\Contracts\Foundation\Application;

function makeRoad($road) {
    return explode(' ', $road);
}
function calc($road, $enter, $exit) {
    $min = 99999999999;
    for($i=$enter ; $i<=$exit ; $i++) {
        if ($road[$i]<$min)
            $min = $road[$i];
    }
    //$relevantRoad = array_slice($road, $enter, $exit-$enter);
    return $min;
}

$handle = fopen ("php://stdin","r");

$data = trim(fgets($handle));
$data = explode(' ', $data);

$roadSize = $data[0];
$testsAmount = $data[1];

$roadString = trim(fgets($handle));
$road = makeRoad($roadString);

while ($test = trim(fgets($handle))) {
    $test = explode(' ', $test);
    echo calc($road, $test[0], $test[1]).PHP_EOL;
}


//echo calc(makeRoad('1 2 2 2 1'), 1, 4).PHP_EOL;

fclose($handle);