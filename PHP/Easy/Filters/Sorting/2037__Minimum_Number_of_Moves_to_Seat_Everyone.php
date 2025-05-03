<?php
function minMovesToSeat($seats, $students)
{
    sort($seats);
    sort($students);

    $total = 0;
    for ($i = 0; $i < count($students); $i++) {
        $total += abs($students[$i] - $seats[$i]);
    }
    return $total;
}
$seats = [3,1,5];
$students = [2,7,4];

echo minMovesToSeat($seats, $students);