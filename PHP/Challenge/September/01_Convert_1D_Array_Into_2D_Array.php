<?php
function construct2DArray($original, $m, $n)
{
    if (count($original) != $m * $n) {
        return [];
    }

    $result = [];
    for ($i = 0;  $i < $m; $i++) {
        $slice = array_slice($original, $i * $n, $n);
        $result[] = $slice;
    }
    return $result;
}