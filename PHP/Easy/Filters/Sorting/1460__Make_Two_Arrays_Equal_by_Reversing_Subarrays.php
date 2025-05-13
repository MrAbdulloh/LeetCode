<?php
function canBeEqual($target, $arr): bool
{
    return array_count_values($target) == array_count_values($arr);
}

$target = [1, 2, 3, 4];
$arr = [2, 4, 1, 3];
var_dump(canBeEqual($target, $arr));