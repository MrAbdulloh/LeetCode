<?php
function minimumAverage($nums)
{
    sort($nums);
    $averages = [];

    while (count($nums) > 0) {
        $min_num = array_shift($nums);
        $max_num = array_pop($nums);
        $averages[] = ($min_num + $max_num) / 2;
    }

    return min($averages);
}

$nums = [7, 8, 3, 4, 15, 13, 4, 1];
echo minimumAverage($nums);