<?php
//https://leetcode.com/problems/removing-stars-from-a-string/description/

function removeStars($s)
{
    $stack = [];
    foreach (str_split($s) as $char) {
        if ($char == '*')
            array_pop($stack);
        else {
            array_push($stack, $char);
        }
    }
    return join($stack);
}

$s = "leet**cod*e";
$s = "erase*****";
echo removeStars($s);