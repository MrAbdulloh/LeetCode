<?php
function makeFancyString($s)
{

    $result = '';
    $count = 0;
    for ($i = 0; $i < strlen($s); $i++) {
        if ($s[$i] == $s[$i - 1]) {
            $count++;
        } else {
            $count = 1;
        }
        if ($count < 3) {
            $result .= $s[$i];
        }
    }
    return $result;
}