#!/usr/bin/env perl
use feature qw(say);
use List::Util 'min';

sub fully_react {
    my ($polymer) = @_;
    do {
        $count = $polymer =~ s/(.)(?!\1)(?i)(\1)//g;
    } while ($count);
    return $polymer;
}

sub reduce {
    my ($polymer, $unit) = @_;
    $polymer =~ s/$unit//gi;
    return $polymer;
}


my $input = <>;
$input =~ s/^\s+|\s+$//g;

my $reacted_input = fully_react $input;
say length $reacted_input;

my @unit_types = split //, (lc $input) =~ s/(.)(?=.*?\1)//rg;
my @lengths;
for my $unit (@unit_types) {
    push @lengths, length(fully_react(reduce($reacted_input, $unit)))
}
say min @lengths
