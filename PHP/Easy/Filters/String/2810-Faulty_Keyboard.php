<?php
function finalString($s)
{
    $result = [];
    for ($i = 0; $i < strlen($s); $i++) {

        if ($s[$i] == 'i') {
            $result =  array_reverse($result);
        } else {
            $result[] = $s[$i];
        }

    }
    return join($result);
}

$s = 'string';
print_r(finalString($s));
//echo finalString($s);