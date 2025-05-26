<?php
function relativeSortArray($arr1, $arr2) {
    $count = array_count_values($arr1);
    $result = [];

    foreach ($arr2 as $num) {
        if (isset($count[$num])) {
            $result = array_merge($result, array_fill(0, $count[$num], $num));
            unset($count[$num]);
        }
    }

    $remaining = array_keys($count);
    sort($remaining);

    foreach ($remaining as $num) {
        $result = array_merge($result, array_fill(0, $count[$num], $num));
    }

    return $result;
}

$arr1 = [2,3,1,3,2,4,6,7,9,2,19];
$arr2 = [2,1,4,3,9,6];
print_r(relativeSortArray($arr1, $arr2));