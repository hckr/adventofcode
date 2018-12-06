#!/usr/bin/env php
<?php

function fully_react($polymer) {
    do {
        $polymer = preg_replace('/(.)(?!\1)(?i)(\1)/', '', $polymer, -1, $count);
    } while ($count);
    return $polymer;
}

function reduce($polymer, $unit) {
    return preg_replace("/$unit/i", '', $polymer);
}


$input = trim(stream_get_contents(STDIN));
$reacted_input = fully_react($input);
echo strlen($reacted_input) . PHP_EOL;

$unit_types = array_unique(str_split(strtolower($input)));
$lengths = [];
foreach ($unit_types as $unit) {
    $lengths[] = strlen(fully_react(reduce($reacted_input, $unit)));
}
echo min($lengths) . PHP_EOL;
