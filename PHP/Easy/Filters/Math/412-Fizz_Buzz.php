<?php
function fizzBuzz($n)
{
    $ans = [];
    for ($i = 1; $i <= $n; $i++) {
        if ($i % 3 == 0 and ($i % 5 == 0)) {
            $ans[] = 'FizzBuzz';
        } else if ($i % 3 == 0) {
            $ans[] = 'Fizz';
        } else if ($i % 5 == 0) {
            $ans[] = 'Buzz';
        }
        else {
            $ans[] = (string) $i;
        }
    }
    return $ans;

}

print_r(fizzBuzz(3));