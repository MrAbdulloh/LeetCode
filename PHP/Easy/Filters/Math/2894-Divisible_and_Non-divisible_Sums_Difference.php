<?php
// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
function differenceOfSums($n, $m)
{
    $a = 0;
    $b = 0;
    for ($i = 1; $i <= $n; $i++) {
        if ($i % $m == 0) {
            $a += $i;
        } else {
            $b += $i;
        }
    }
    return $b - $a;

}

echo differenceOfSums(10, 3);