<?php
//https://leetcode.com/problems/two-sum/description/

function twoSum($nums, $target)
{
    $num_dict = [];
    foreach ($nums as $i => $num) {
        $complement = $target - $num;
        if (array_key_exists($complement, $num_dict)) {
            return [$num_dict[$complement], $i];
        }
        $num_dict[$num] = $i;
    }
    return [];
}

$nums = [2, 7, 11, 15];
$target = 9;
$result = twoSum($nums, $target);
print_r($result);