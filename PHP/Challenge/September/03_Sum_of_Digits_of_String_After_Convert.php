<?php
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03
function getLucky($s, $k) {
    $num_str = "";
    $length = strlen($s);

    for ($i = 0; $i < $length; $i++) {
        $char = $s[$i];
        $char_value = ord($char) - ord('a') + 1;
        $num_str .= $char_value;
    }

    for ($j = 0; $j < $k; $j++) {
        $new_sum = 0;
        $length = strlen($num_str);

        for ($i = 0; $i < $length; $i++) {
            $new_sum += intval($num_str[$i]);
        }

        $num_str = strval($new_sum);
    }

    return intval($num_str);
}

$s = "zbax";
$k = 2;
echo getLucky($s, $k);