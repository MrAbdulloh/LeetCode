<?php
function countGoodTriplets($arr, $a, $b, $c)
{
    $count = 0;
    $len = count($arr);
    for ($i = 0; $i < $len; $i++) {
        for ($j = $i + 1; $j < $len; $j++) {
            for ($k = $j + 1; $k < $len; $k++) {
                if (
                    abs($arr[$i] - $arr[$j]) <= $a &&
                    abs($arr[$j] - $arr[$k]) <= $b &&
                    abs($arr[$i] - $arr[$k]) <= $c
                ) {
                    $count++;
                }
            }
        }
    }
    return $count;
}

$arr = [3, 0, 1, 1, 9, 7];
$a = 7;
$b = 2;
$c = 3;
echo countGoodTriplets($arr, $a, $b, $c);