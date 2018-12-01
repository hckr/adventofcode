#!/usr/bin/env perl

$frequency = 0;
$previous_frequencies{$frequency} = 1;

@changes = <>;

while(1) {
    foreach $change (@changes) {
        $frequency += $change;
        if (exists $previous_frequencies{$frequency}) {
            print $frequency;
            exit;
        }
        $previous_frequencies{$frequency} = 1;
    }
}
