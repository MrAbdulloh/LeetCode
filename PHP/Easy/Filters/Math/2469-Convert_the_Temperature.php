<?php

// https://leetcode.com/problems/convert-the-temperature/

function convertTemperature($celsius)
{
    return [$celsius + 273.15, $celsius * 1.80 + 32.00];
}