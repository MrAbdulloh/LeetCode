<?php
function arithmeticTriplets($nums, $diff)
{
    $count = 0;
    for ($i = 0; $i < count($nums); $i++) {
        for ($j = $i + 1; $j < count($nums); $j++) {
            if ($nums[$j] - $nums[$i] == $diff) {
                for ($k = $i + 1; $k < count($nums); $k++) {
                    if ($nums[$k] - $nums[$j] == $diff) {
                        $count += 1;
                    }
                }
            }
        }
    }
    return $count;
}


$nums = [0, 1, 4, 6, 7, 10];
$diff = 3;
echo arithmeticTriplets($nums, $diff);
