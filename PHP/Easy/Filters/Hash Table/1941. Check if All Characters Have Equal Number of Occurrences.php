<?php
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
function areOccurrencesEqual($s)
{
    $count = [];
    foreach (str_split($s) as $c) {
        if (array_key_exists($c, $count)) {
            $count[$c] += 1;
        } else {
            $count[$c] = 1;
        }
    }
    $fre = array_values($count);
    foreach ($fre as $i) {
        if ($i !== $fre[0]) {
            return false;
        }
    }
    return true;

}


$s = "aabb";
print_r(areOccurrencesEqual($s));