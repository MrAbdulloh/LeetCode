<?php
function deleteGreatestValue($grid)
{
    foreach ($grid as &$row) {
        sort($row);
    }

    $answer = 0;
    $n = count($grid[0]);
    for ($col = 0; $col < $n; $col++) {
        $maxDeleted = 0;
        foreach ($grid as &$row) {
            $maxDeleted = max($maxDeleted, array_pop($row));
        }
        $answer += $maxDeleted;
    }
    return $answer;
}

$grid = [[1, 2, 4], [3, 3, 1]];
echo deleteGreatestValue($grid);