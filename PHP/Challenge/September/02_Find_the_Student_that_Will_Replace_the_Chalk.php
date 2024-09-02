<?php
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/?envType=daily-question&envId=2024-09-02

function chalkReplacer($chalk, $k)
{
    $total_sum = array_sum($chalk);
    $k %= $total_sum;
    for ($i = 0; $i < count($chalk); $i++) {
        if ($k < $chalk[$i]) {
            return $i;
        }
        $k -= $chalk[$i];
    }
}

//$chalk = [5, 1, 5];
//$k = 22;
$chalk = [3, 4, 1, 2];
$k = 25;
echo chalkReplacer($chalk, $k);