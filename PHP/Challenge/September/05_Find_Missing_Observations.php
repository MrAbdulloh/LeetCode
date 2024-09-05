<?php
//function missingRolls($rolls, $mean, $n)
//{
//    $m = count($rolls);
//    $total_sum = $mean * ($n + $m);
//    $current_sum = array_sum($rolls);
//    $missing_sum = $total_sum - $current_sum;
//
//    if ($missing_sum < $n or $missing_sum > 6 * $n) {
//        return [];
//    }
//
//    $base_value = intdiv($missing_sum, $n);
//    $result = array_fill(0, $n, $base_value);
//    $remainder = $missing_sum % $n;
//
//    for ($i = 1; $i < $remainder; $i++) {
//        $result[$i] += 1;
//    }
//    return $result;
//}
function missingRolls($rolls, $mean, $n)
{
    $m = count($rolls);
    $total_sum = $mean * ($n + $m);
    $current_sum = array_sum($rolls);
    $missing_sum = $total_sum - $current_sum;

    if ($missing_sum < $n || $missing_sum > 6 * $n) {
        return [];
    }

    $base_value = intdiv($missing_sum, $n);
    $result = array_fill(0, $n, $base_value);
    $remainder = $missing_sum % $n;

    for ($i = 0; $i < $remainder; $i++) {
        $result[$i] += 1;
    }

    return $result;
}

$rolls = [1, 5, 6];
$mean = 3;
$n = 4;

//$rolls = [3, 2, 4, 3];
//$mean = 4;
//$n = 2;
print_r(missingRolls($rolls, $mean, $n));