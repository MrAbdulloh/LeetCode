<?php
 // https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
function maximumTripletValue($nums) {
    $n = count($nums);
    $maxValue = 0;

    for ($i = 1; $i < $n - 1; $i++) {
        $maxLeft = max(array_slice($nums, 0, $i));
        $maxRight = max(array_slice($nums, $i + 1));

        $value = ($maxLeft - $nums[$i]) * $maxRight;
        $maxValue = max($maxValue, $value);
    }
    return $maxValue > 0 ? $maxValue : 0;
}