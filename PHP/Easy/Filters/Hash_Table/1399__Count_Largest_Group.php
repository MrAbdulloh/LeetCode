<?php
function countLargestGroup($n)
{
    $groups = [];
    for ($num = 1; $num <= $n; $num++) {
        $digit_sum = array_sum(str_split((string)$num));
        $groups[$digit_sum] = ($groups[$digit_sum] ?? 0) + 1;
    }
    $max_size = max($groups);
    $count = count(array_filter($groups, fn($size) => $size == $max_size));

    return $count;
}

$n = 13;
echo countLargestGroup($n);