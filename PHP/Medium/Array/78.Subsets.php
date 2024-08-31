<?php
function subsets($nums)
{
    $result = [[]];

    foreach ($nums as $num) {
        $newSubsets = [];

        foreach ($result as $subset) {
            $newSubset = $subset;
            $newSubset[] = $num;
            $newSubsets[] = $newSubset;
        }
        $result = array_merge($result, $newSubsets);
    }
    return $result;
}


$num = [1, 2, 3];
print_r(subsets($num));