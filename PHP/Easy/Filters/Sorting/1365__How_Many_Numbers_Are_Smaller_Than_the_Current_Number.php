<?php

function smallerNumbersThanCurrent($nums)
{
    $result = [];
    $s = $nums;
    sort($s);

    foreach ($nums as $num) {
        $result [] = array_search($num, $s);
    }
    return $result;
}

$nums = [8, 1, 2, 2, 3];
print_r(smallerNumbersThanCurrent($nums));