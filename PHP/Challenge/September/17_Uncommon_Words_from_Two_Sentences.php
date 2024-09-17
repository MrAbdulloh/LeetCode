<?php
//https://leetcode.com/problems/uncommon-words-from-two-sentences/description/?envType=daily-question&envId=2024-09-17
function uncommonFromSentences($s1, $s2): array
{
    $combinedWords = array_merge(explode(' ', $s1), explode(' ', $s2));
    $wordCount = array_count_values($combinedWords);
    $uncommonWords = array_filter($wordCount, function ($count) {
        return $count === 1;
    });

    return array_keys($uncommonWords);
}

$s1 = "apple banana apple";
$s2 = "banana orange grape";

$result = uncommonFromSentences($s1, $s2);
print_r($result);