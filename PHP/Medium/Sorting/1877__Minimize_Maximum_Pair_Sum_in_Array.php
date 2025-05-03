<?php
function minPairSum($nums)
{
    sort($nums);
    $len = count($nums);
    $max_pair_sum = 0;
    for ($i = 0; $i < $len / 2; $i++) {
        $pair_sum = $nums[$i] + $nums[$len - 1 - $i];
        $max_pair_sum = max($max_pair_sum, $pair_sum);
    }
    return $max_pair_sum;
}

$nums = [4, 1, 5, 1, 2, 5, 1, 5, 5, 4];
echo minPairSum($nums);
