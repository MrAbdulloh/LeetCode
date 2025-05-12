<?php
function maxSatisfaction($satisfaction) :int
{
    rsort($satisfaction);
    $total = 0;
    $prefix_sum = 0;

    foreach ($satisfaction as $value) {
        if ($prefix_sum + $value >= 0) {
            $prefix_sum += $value;
            $total += $prefix_sum;
        } else {
            break;
        }
    }
    return $total;

}

$satisfaction = [-1, -8, 0, 5, -7];
echo (maxSatisfaction($satisfaction));