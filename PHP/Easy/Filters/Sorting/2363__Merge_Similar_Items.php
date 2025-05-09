<?php
function mergeSimilarItems($items1, $items2)
{
    $valueWeightMap = [];

    foreach ($items1 as $item) {
        $value = $item[0];
        $weight = $item[1];

        if (!isset($valueWeightMap[$value])) {
            $valueWeightMap[$value] = 0;
        }
        $valueWeightMap[$value] += $weight;
    }

    foreach ($items2 as $item) {
        $value = $item[0];
        $weight = $item[1];

        if (!isset($valueWeightMap[$value])) {
            $valueWeightMap[$value] = 0;
        }
        $valueWeightMap[$value] += $weight;
    }

    ksort($valueWeightMap);

    $result = [];
    foreach ($valueWeightMap as $value => $weight) {
        $result[] = [$value, $weight];
    }

    return $result;
}

$items1 = [[1, 1], [4, 5], [3, 8]];
$items2 = [[3, 1], [1, 5]];

print_r(mergeSimilarItems($items1, $items2));