<?php
function largestSubmatrix($matrix)
{
    $m = count($matrix);
    $n = count($matrix[0]);

    for ($i = 1; $i < $m; $i++) {
        for ($j = 0; $j < $n; $j++) {
            if ($matrix[$i][$j] == 1) {
                $matrix[$i][$j] += $matrix[$i - 1][$j];
            }
        }
    }
    $max_area = 0;
    foreach ($matrix as &$row) {
        rsort($row);
        for ($j = 0; $j < $n; $j++) {
            $max_area = max($max_area, $row[$j] * ($j + 1));
        }
    }
    return $max_area;
}

echo largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]);
echo largestSubmatrix([[1, 1, 0], [1, 0, 1]]);