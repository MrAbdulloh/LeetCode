<?php
function subsetXORSum($nums) {
    $dfs = function ($i, $current_xor) use ($nums, &$dfs) {
        if ($i == count($nums)) {
            return $current_xor;
        }
        return $dfs($i + 1, $current_xor ^ $nums[$i]) + $dfs($i + 1, $current_xor);
    };

    return $dfs(0, 0);
}

echo subsetXORSum([1, 3]);

