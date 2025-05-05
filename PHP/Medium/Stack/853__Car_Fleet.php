<?php
// https://leetcode.com/problems/car-fleet/
function carFleet($target, $position, $speed) {
    $cars = array_map(null, $position, $speed);
    usort($cars, function ($a, $b) {return $b[0] <=> $a[0];});

    $stack = [];
    foreach ($cars as $car) {
        $pos = $car[0];
        $spd = $car[1];
        $time = ($target - $pos) / $spd;

        if (empty($stack) || $time > end($stack)) {
            $stack[] = $time;
        }
    }
    return count($stack);

}