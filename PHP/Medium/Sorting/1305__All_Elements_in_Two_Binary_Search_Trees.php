<?php

class TreeNode
{
    public function __construct(public $val = 0, public $left = null, public $right = null)
    {
    }
}

class Solution
{
    function inorderTraversal($root, &$result)
    {
        if ($root === null) {
            return;
        }
        $this->inorderTraversal($root->left, $result);
        $result[] = $root->val;
        $this->inorderTraversal($root->right, $result);
    }

    function mergeSortedLists($list1, $list2)
    {
        $merged = [];
        $i = 0;
        $j = 0;
        while ($i < count($list1) && $j < count($list2)) {
            if ($list1[$i] < $list2[$j]) {
                $merged[] = $list1[$i++];
            } else {
                $merged[] = $list2[$j++];
            }
        }
        while ($i < count($list1)) {
            $merged[] = $list1[$i++];
        }
        while ($j < count($list2)) {
            $merged[] = $list2[$j++];
        }
        return $merged;
    }

    function getAllElements($root1, $root2)
    {
        $list1 = [];
        $list2 = [];
        $this->inorderTraversal($root1, $list1);
        $this->inorderTraversal($root2, $list2);

        return $this->mergeSortedLists($list1, $list2);
    }
}
