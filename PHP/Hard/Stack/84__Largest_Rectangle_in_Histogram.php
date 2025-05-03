<?php
function largestRectangleArea($heights)
{
    $stack = [];
    $maxArea = 0;
    $heights[] = 0;

    for ($i = 0; $i < count($heights); $i++) {
        while (!empty($stack) && $heights[$i] < $heights[end($stack)]) {
            $h = $heights[array_pop($stack)];
            $w = $i - (empty($stack) ? 0 : end($stack) + 1);
            $maxArea = max($maxArea, $h * $w);
        }
        $stack[] = $i;
    }

    return $maxArea;
}

$heights = [2, 1, 5, 6, 2, 3];
echo largestRectangleArea($heights);