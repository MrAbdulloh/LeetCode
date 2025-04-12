<?php
// https://leetcode.com/problems/intersection-of-two-arrays/description/

//function intersection($nums1, $nums2)
//{
//    $data = array_intersect($nums1, $nums2);
//    $result = array_count_values($data);
//    return array_keys($result);
//}

function intersection($nums1, $nums2)
{
    return array_values(array_unique(array_intersect($nums1, $nums2)));
}

//$nums1 = [1, 2, 2, 1];
//$nums2 = [2, 2];
$nums1 = [4,9,5];
$nums2 = [9,4,9,8,4];
print_r(intersection($nums1, $nums2));