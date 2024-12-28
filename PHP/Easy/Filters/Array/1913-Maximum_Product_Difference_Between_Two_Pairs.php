<?php
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
function maxProductDifference($nums)
{
    sort($nums);
    return ($nums[count($nums) - 1] * $nums[count($nums) - 2]) - ($nums[0] * $nums[1]);
}


$nums = [5, 6, 2, 7, 4];
echo maxProductDifference($nums);