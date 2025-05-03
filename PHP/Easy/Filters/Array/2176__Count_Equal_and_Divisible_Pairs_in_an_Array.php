<?php
function countPairs($nums, $k)
{
    $len = count($nums);
    $count = 0;
    for ($i = 0; $i < $len - 1; $i++) {
        for ($j = $i + 1; $j < $len; $j++) {
            if ($nums[$i] == $nums[$j] and ($i * $j) % $k == 0) {
                $count++;
            }
        }
    }
    return $count;
}
$nums = [3, 1, 2, 2, 2, 1, 3];
$k = 2;