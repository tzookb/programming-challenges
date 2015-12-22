<?php

function solution($arr) {
	$counter = 0;
	$size = sizeof($arr);
	$location = 0;	//starting linked list location

    while ($counter++ < $size) {
    	$location = $arr[$location];
    	
    	if ($location == -1) {
    		break;
    	}

    }

    if ($counter == $size+1)
    	return -1;

    return $counter;
}