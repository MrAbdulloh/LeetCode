<?php
//https://leetcode.com/problems/group-anagrams/description/

function groupAnagrams($strs)
{
    $anagrams = [];
    foreach ($strs as $str) {
        $key = str_split($str);
        sort($key);
        $key = implode("", $key);

        if (!isset($anagrams[$key])) {
            $anagrams[$key] = [];
        }
        $anagrams[$key][] = $str;
    }
    return array_values($anagrams);
}

$strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
var_dump(groupAnagrams($strs));
