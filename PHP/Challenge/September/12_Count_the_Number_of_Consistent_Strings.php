<?php
// https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=daily-question&envId=2024-09-12
function countConsistentStrings($allowed, $words)
{
    $count = 0;
    foreach ($words as $word) {
        $count ++;
        foreach (str_split($word) as $letter) {
            if (strpos($allowed, $letter) === false) {
                $count --;
                break;
            }
        }
    }
    return $count;
}