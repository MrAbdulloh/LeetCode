<?php
function canPartition($nums)
{
    $total = array_sum($nums);
    if ($total % 2 != 0) {
        return false;
    }

    $target = (int)$total / 2;
    $dp = array_fill(0, $target + 1, false);
    $dp[0] = true;

    foreach ($nums as $num) {
        for ($i = $target; $i >= $num; $i--) {
            $dp[$i] = $dp[$i] || $dp[$i - $num];
        }
    }
    return $dp[$target];
}

$nums = [1, 5, 11, 5];
echo canPartition($nums);