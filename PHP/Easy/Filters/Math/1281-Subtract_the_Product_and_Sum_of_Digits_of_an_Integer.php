<?php
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
function subtractProductAndSum($n)
{
    $possibleSum = 0;
    $a = 1;
    foreach (str_split($n) as $c) {
        $possibleSum += $c;
        $a *= $c;
    }
    return $a - $possibleSum;

}

$n = 234;
var_dump(subtractProductAndSum($n));