<?php

function threeConsecutiveOdds($arr)
{
    $result = 0;
    foreach ($arr as $value) {
        if ($value % 2 == 1) {
            $result += 1;
            if ($result == 3) {
                return true;
            }
        } else {
            $result = 0;
        }

    }
    return false;
}

$arr = [1, 2, 34, 3, 4, 5, 7, 23, 12];
var_dump(threeConsecutiveOdds($arr));
