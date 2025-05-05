<?php

function minimumPushes(string $word): int
{
    $freq = array_count_values(str_split($word));
    arsort($freq);
    $sort_freq = array_values($freq);

    $total_pushes = 0;
    foreach ($sort_freq as $i => $count) {
        $pushes = (int)($i / 8) + 1;
        $total_pushes += $count * $pushes;
    }
    return $total_pushes;
}

$word = "abcde";
echo minimumPushes($word);