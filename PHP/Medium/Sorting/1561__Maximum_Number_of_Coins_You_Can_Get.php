<?php
//function maxCoins($piles)
//{
//    rsort($piles);
//    $count = 0;
//    while (!empty($piles)) {
//        array_shift($piles);
//        $count += array_shift($piles);
//        array_pop($piles);
//    }
//    return $count;
//}

function maxCoins($piles)
{
    rsort($piles);
    $count = 0;
    $n = count($piles) / 3;

    for ($i = 0; $i < $n; $i++) {
        $count += $piles[$i * 2 + 1];
    }

    return $count;
}

$piles = [2, 4, 1, 2, 7, 8];
var_dump(maxCoins($piles));