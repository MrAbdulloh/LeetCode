<?php
function removeTrailingZeros($num)
{
    return trim($num, "0");
}

$str = "51230100";
echo removeTrailingZeros($str);