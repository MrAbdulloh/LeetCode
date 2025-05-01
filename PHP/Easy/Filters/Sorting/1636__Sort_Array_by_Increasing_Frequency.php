<?php
function frequencySort($nums) {
    $freq = array_count_values($nums);

    usort($nums, function($a, $b) use ($freq) {
        if ($freq[$a] == $freq[$b]) {
            return $b - $a;
        }
        return $freq[$a] - $freq[$b];
    });

    return $nums;
}

$nums = [2, 3, 1, 3, 2];
print_r(frequencySort($nums));