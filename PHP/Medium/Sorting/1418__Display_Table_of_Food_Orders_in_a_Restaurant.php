<?php
function displayTable($orders)
{
    $foodItems = [];
    $tableOrders = [];

    foreach ($orders as $order) {
        list($customer, $table, $food) = $order;
        $foodItems[$food] = true;
        if (!isset($tableOrders[$table])) {
            $tableOrders[$table] = [];
        }
        if (!isset($tableOrders[$table][$food])) {
            $tableOrders[$table][$food] = 0;
        }
        $tableOrders[$table][$food]++;
    }

    ksort($foodItems);
    $sortedFoodItems = array_keys($foodItems);

    $result = [];
    $header = array_merge(["Table"], $sortedFoodItems);
    $result[] = $header;

    ksort($tableOrders, SORT_NUMERIC);
    foreach ($tableOrders as $table => $foodCounts) {
        $row = [$table];
        foreach ($sortedFoodItems as $food) {
            $row[] = isset($foodCounts[$food]) ? strval($foodCounts[$food]) : "0";
        }
        $result[] = $row;
    }

    return $result;
}

$orders = [
    ["David", "3", "Ceviche"],
    ["Corina", "10", "Beef Burrito"],
    ["David", "3", "Fried Chicken"],
    ["Carla", "5", "Water"],
    ["Carla", "5", "Ceviche"],
    ["Rous", "3", "Ceviche"]
];

var_dump(displayTable($orders));