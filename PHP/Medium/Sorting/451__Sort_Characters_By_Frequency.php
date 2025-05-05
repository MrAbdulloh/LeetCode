<?php
function frequencySort($s) {
    $charCount = array_count_values(str_split($s));
    arsort($charCount);

    $result = '';
    foreach ($charCount as $char => $count) {
        $result .= str_repeat($char, $count);
    }
    return $result;
}

echo frequencySort("tree");
//echo frequencySort("Aabb");