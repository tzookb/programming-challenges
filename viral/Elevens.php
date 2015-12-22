<?php

function solution($n) {
    if ($n == 0)    return 1;

    $value = '1';
    while ($n-- > 0) {
        //representing results as strings
        $by1 = $value;
        $by10 = $value.'0';
        $value = $by10;


        //now Ill add results together
        $size = strlen($by10);
        $extra = 0;
        
        

        while ($size > 0) {
            $by1Val = isset($by1[$size-2])? intval($by1[$size-2]) : 0;

            $intRes = intval($by10[$size-1])+$by1Val+$extra;
            if ($intRes > 9) {
                $extra = 1;
                $remainder = $intRes - 10;
            } else {
                $extra = 0;
                $remainder = $intRes;
            }
            $value[$size-1] = $remainder;

            $size--;
        }

        if ($extra == 1) {
            //biggest digit needs one more
            $res = intval($value[0])+1;
            if ($res>9) {
                $value = $res+''+substr($value, 1);
            } else {
                $value[0] = $res;
            }
        }

        
    }
    return substr_count($value, '1');

}

$res = solution(11);

echo $res;