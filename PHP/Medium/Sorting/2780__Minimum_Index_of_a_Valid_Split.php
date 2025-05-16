<?php
function minimumIndex($nums)
{
    $n = count($nums);
    $freq = array_count_values($nums);
    arsort($freq);
    $dominant = array_key_first($freq);

    $countLeft = 0;
    $countTotal = $freq[$dominant];

    for ($i = 0; $i < $n - 1; $i++) {
        if ($nums[$i] == $dominant) {
            $countLeft++;
        }
        if ($countLeft * 2 > ($i + 1) && ($countTotal - $countLeft) * 2 > ($n - $i - 1)) {
            return $i;
        }
    }
    return -1;
}

$nums1 = [1, 2, 2, 2];

echo minimumIndex($nums1);