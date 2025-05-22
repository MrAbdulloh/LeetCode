<?php
function findKthLargest($nums, $k)
{
    sort($nums);
    $split = array_slice($nums, -$k)[0];
    return $split;
}

$nums = [3, 2, 1, 5, 6, 4];
$k = 2;
var_dump(findKthLargest($nums, $k));