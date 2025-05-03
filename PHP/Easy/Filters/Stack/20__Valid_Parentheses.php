<?php

function isValid($s)
{
    $stack = [];
    $map = ['(' => ')', '{' => '}', '[' => ']'];

    for ($i = 0; $i < strlen($s); $i++) {
        $ch = $s[$i];
        if (isset($map[$ch])) {
            $stack[] = $ch;
        } else {
            if (!empty($stack) && $map[end($stack)] === $ch) {
                array_pop($stack);
            } else {
                return false;
            }
        }
    }
    return empty($stack);
}

$s = "()";
var_dump(isValid($s));