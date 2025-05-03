<?php
function checkArithmeticSubarrays($nums, $l, $r)
{
    $answer = [];
    for ($i = 0; $i < count($l); $i++) {
        $subarray = array_slice($nums, $l[$i], $r[$i] - $l[$i] + 1);
        sort($subarray);
        $is_arithmetic = true;
        $diff = $subarray[1] - $subarray[0];
        for ($j = 1; $j < (count($subarray) - 1); $j++) {
            if ($subarray[$j + 1] - $subarray[$j] != $diff) {
                $is_arithmetic = false;
                break;
            }
        }
        $answer[] = $is_arithmetic;
    }
    return $answer;
}
$nums = [4, 6, 5, 9, 3, 7];
$l = [0, 0, 2];
$r = [2, 3, 5];

var_dump(checkArithmeticSubarrays($nums, $l, $r));