<?php
// https://leetcode.com/problems/counting-words-with-a-given-prefix/description/
function prefixCount($words, $pref)
{
    $count = 0;
    foreach ($words as $word) {
        if (substr($word, 0, strlen($pref)) == $pref) {
            $count++;
        }

    }
    return $count;

}

$words = ["pay", "attention", "practice", "attend"];
$pref = "at";
echo prefixCount($words, $pref);