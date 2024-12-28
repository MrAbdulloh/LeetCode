<?php

// https://leetcode.com/problems/smallest-even-multiple/
class Solution
{

    /**
     * @param Integer $n
     * @return Integer
     */
    function smallestEvenMultiple($n)
    {
        return $n % 2 === 0 ? $n : $n * 2;
    }
}

$obj = new Solution();
$result = $obj->smallestEvenMultiple(5);
echo $result;