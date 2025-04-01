<?php
//https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2024-09-18
function largestNumber($nums)
{
    $nums = array_map('strval', $nums);

    usort($nums, function ($x, $y) {
        if ($x . $y > $y . $x) {
            return -1;
        } elseif ($x . $y < $y . $x) {
            return 1;
        } else {
            return 0;
        }
    });
    $result = implode('', $nums);

    return $result[0] === '0' ? '0' : $result;
}

$nums = [10, 2];
echo largestNumber($nums);