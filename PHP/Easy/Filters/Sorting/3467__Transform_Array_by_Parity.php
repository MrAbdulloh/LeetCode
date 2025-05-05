<?php
// https://leetcode.com/problems/transform-array-by-parity/description/

function transformArray($nums)
{
    $result = [];
    foreach ($nums as $num) {
        if ($num % 2 == 0) {
            $result[] = 0;
        } else {
            $result[] = 1;
        }
    }
    sort($result);
    return $result;
}

//$nums = [4,3,2,1];
$nums = [1,5,1,4,2];
print_r(transformArray($nums));