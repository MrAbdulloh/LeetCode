<?php

function sortVowels($s)
{
    $chars = str_split($s);
    $vowels = [];

    foreach ($chars as $char) {
        if (strpos('aeiouAEIOU', $char) !== false) {
            $vowels[] = $char;
        }
    }
    sort($vowels);
    $vowelIndex = 0;

    foreach ($chars as $i => $char) {
        if (strpos("aeiouAEIOU", $char) !== false) {
            $chars[$i] = $vowels[$vowelIndex++];
        }
    }
    return implode('', $chars);
}

$word = "lEetcOde";
var_dump(sortVowels($word));