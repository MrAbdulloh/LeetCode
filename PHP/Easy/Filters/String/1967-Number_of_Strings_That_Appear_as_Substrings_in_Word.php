<?php
function numOfStrings($patterns, $word)
{
    $count = 0;
    foreach ($patterns as $pattern) {
        if (strpos($word, $pattern) !== false) {
            $count += 1;
        }
    }
    return $count;
}

$patterns = ["a", "abc", "bc", "d"];
$word = "abc";
echo numOfStrings($patterns, $word);