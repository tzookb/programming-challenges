<?php

function solution(&$A, &$B) {
    $n = sizeof($A);
    $m = sizeof($B);
    sort($A);
    sort($B);
    $i = 0;
    for ($k = 0; $k < $n; $k++) {
        if ($i < $m - 1 AND $B[$i] < $A[$k])
            $i += 1;
        if ($A[$k] == $B[$i])
            return $A[$k];
    }
    return -1;
}