<?php
function countKeyChanges($s) {
    $l = strlen($s);
    $ss = strtolower($s);
    $n = 1;
    $m = 0;
    $ans = 0;
    while ($n < $l) {
        if ($ss[$m] != $ss[$n]) {
            $ans ++;
        }
        $n ++;
        $m ++;
    }
    return $ans;

}

$s = "aAbBcC";
echo countKeyChanges($s);