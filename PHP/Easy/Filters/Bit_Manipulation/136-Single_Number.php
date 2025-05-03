<?php
//function singleNumber($nums)
//{
//    $result = 0;
//    foreach ($nums as $num) {
//        $result ^= $num;
//    }
//    return $result;
//}
function singleNumber($nums)
{
    $count = [];
    foreach ($nums as $num) {
        if (array_key_exists($num, $count)) {
            $count[$num] += 1;
        } else {
            $count[$num] = 1;
        }
    }
    foreach ($count as $num => $value) {
        if ($value = 1) {
            return $num;
        }
    }
}

$nums = [4, 1, 2, 1, 2];
echo "\n";
print_r(singleNumber($nums));
echo "\n";