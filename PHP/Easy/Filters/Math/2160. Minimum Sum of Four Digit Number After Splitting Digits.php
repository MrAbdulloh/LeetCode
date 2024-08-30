<?php
// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

function minimumSum($num)
{
    $a = str_split($num);
    sort($a);
    return intval($a[0] . $a[2]) + intval($a[1] . $a[3]);

}

echo minimumSum(4009);