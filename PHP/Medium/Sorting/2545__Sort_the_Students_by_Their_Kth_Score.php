<?php
function sortTheStudents($score, $k)
{
    usort($score, function ($a, $b) use ($k) {
        return $b[$k] <=> $a[$k];
    });
    return $score;
}

$score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]];
$k = 2;

var_dump(sortTheStudents($score, $k));