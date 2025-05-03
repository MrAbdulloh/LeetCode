<?php

function subarraySum($nums, $k)
{
    $count = 0;
    $current_sum = 0;
    $prefix_sum = [0 => 1];

    foreach ($nums as $num) {
        $current_sum += $num;

        if (isset($prefix_sum[$current_sum - $k])) {
            $count += $prefix_sum[$current_sum - $k];
        }
        if (isset($prefix_sum[$current_sum])) {
            $prefix_sum[$current_sum]++;
        } else {
            $prefix_sum[$current_sum] = 1;
        }
    }
    return $count;
}

$nums = [1, 1, 1];
$k = 2;
echo subarraySum($nums, $k);