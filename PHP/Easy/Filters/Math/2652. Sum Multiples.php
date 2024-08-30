<?php
// https://leetcode.com/problems/sum-multiples/description/

function sumOfMultiples($n)
{
    $count = 0;
    for ($i = 1; $i <= $n; $i++) {
        if ($i % 3 == 0 or $i % 5 == 0 or $i % 7 == 0) {
            $count += $i;
        }
    }
    return $count;
}