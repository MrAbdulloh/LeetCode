<?php
function mergeAlternately($word1, $word2)
{
    $m = strlen($word1);
    $n = strlen($word2);
    $i = 0;
    $j = 0;
    $res = '';
    while (($i < $m) or ($j < $n)) {
        if ($i < $m) {
            $res .= $word1[$i];
            $i += 1;
        }
        if ($j < $n) {
            $res .= $word2[$j];
            $j += 1;
        }
    }
    return $res;
}