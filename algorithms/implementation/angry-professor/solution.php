<?php

function wouldBeALesson($students, $minToStartClass, $studentsTimes) {
    $studentsTimes = explode(' ', $studentsTimes);
    $onTimeStudents = array_filter($studentsTimes, function($row) {
        return $row<=0;
    });
    if ( sizeof($onTimeStudents) >= $minToStartClass)
        return 'NO';
    return 'YES';
}

$handle = fopen ("php://stdin","r");

$tests = trim(fgets($handle));
$i = 0;

while ($i++ < $tests) {
    $studentsAndMin = trim(fgets($handle));
    $studentsAndMin = explode(' ', $studentsAndMin);
    $studentsTimes = trim(fgets($handle));
    echo wouldBeALesson($studentsAndMin[0], $studentsAndMin[1], $studentsTimes).PHP_EOL;
}



fclose($handle);