<?php
//https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/
function maximumTripletValue($nums)
{
    $n = count($nums);
    if ($n < 3) return 0;

    $leftMax = array_fill(0, $n, 0);
    $leftMax[0] = $nums[0];
    for ($i = 1; $i < $n; $i++) {
        $leftMax[$i] = max($leftMax[$i - 1], $nums[$i]);
    }

    $rightMax = array_fill(0, $n, 0);
    $rightMax[$n - 1] = $nums[$n - 1];
    for ($i = $n - 2; $i >= 0; $i--) {
        $rightMax[$i] = max($rightMax[$i + 1], $nums[$i]);
    }

    $ans = 0;
    for ($i = 1; $i < $n - 1; $i++) {
        $left = $leftMax[$i - 1];
        $right = $rightMax[$i + 1];
        $ans = max($ans, ($left - $nums[$i]) * $right);
    }

    return max($ans, 0);
}