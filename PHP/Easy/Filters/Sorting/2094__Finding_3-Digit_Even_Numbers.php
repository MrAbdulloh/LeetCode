<?php
function findEvenNumbers($digits)
{
    $uniqueNumbers = [];
    $count = array_count_values($digits);

    foreach ($digits as $i) {
        if ($i == 0) continue;
        foreach ($digits as $j) {
            foreach ($digits as $k) {
                if ($k % 2 != 0) continue;
                $num = $i * 100 + $j * 10 + $k;


                $tempCount = [$i => 0, $j => 0, $k => 0];
                foreach ([$i, $j, $k] as $d) {
                    $tempCount[$d]++;
                    if ($tempCount[$d] > ($count[$d] ?? 0)) {
                        continue 2;
                    }
                }

                $uniqueNumbers[$num] = $num;
            }
        }
    }

    sort($uniqueNumbers);
    return array_values($uniqueNumbers);
}

$digits = [2, 1, 3, 0];
print_r(findEvenNumbers($digits));