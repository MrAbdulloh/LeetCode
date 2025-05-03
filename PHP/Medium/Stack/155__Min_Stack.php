<?php
//https://leetcode.com/problems/min-stack/description/
class MinStack
{
    function __construct()
    {
        $this->stack = [];
        $this->min_stack = [];
    }

    function push($val)
    {
        $this->stack[] = $val;

        if (!$this->min_stack || $val <= end($this->min_stack)) {
            $this->min_stack[] = $val;
        }
    }

    function pop()
    {
        if ($this->stack) {
            $top_value = array_pop($this->stack);
            if ($top_value == end($this->min_stack)) {
                array_pop($this->min_stack);
            }
        }
    }

    function top()
    {
        if ($this->stack) {
            return end($this->stack);
        }
    }

    function getMin()
    {
        if ($this->min_stack) {
            return end($this->min_stack);
        }
    }
}
