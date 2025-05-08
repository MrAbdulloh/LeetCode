<?php

function sortByBits($arr)
{
    usort($arr, function($a, $b) {
        $countA = substr_count(decbin($a), '1');
        $countB = substr_count(decbin($b), '1');

        return ($countA === $countB) ? $a - $b : $countA - $countB;
    });

    return $arr;
}