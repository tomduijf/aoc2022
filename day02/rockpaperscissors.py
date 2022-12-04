#!/usr/bin/env python3

ROCK=1
PAPER=2
SCISSORS=3
LOSS=0
TIE=3
WIN=6

# Scoring based on opponent choice vs my choice
SCORING_ONE = {
        'A': { # Rock
            'X': ROCK + TIE,
            'Y': PAPER + WIN,
            'Z': SCISSORS + LOSS},
        'B': { # Paper
            'X': ROCK + LOSS,
            'Y': PAPER + TIE,
            'Z': SCISSORS + WIN},
        'C': { # Scissors
            'X': ROCK + WIN,
            'Y': PAPER + LOSS,
            'Z': SCISSORS + TIE}}

# Scoring based on opponent choice vs intended result (loss/tie/win)
SCORING_TWO = {
        'A': { # Rock
            'X': LOSS + SCISSORS,
            'Y': TIE + ROCK,
            'Z': WIN + PAPER},
        'B': { # Paper
            'X': LOSS + ROCK,
            'Y': TIE + PAPER,
            'Z': WIN + SCISSORS},
        'C': { # Scissors
            'X': LOSS + PAPER,
            'Y': TIE + SCISSORS,
            'Z': WIN + ROCK}}

def matchdata(filename):
    with open(filename) as f:
        for line in f.readlines():
            yield line.split()

print('# Part one # ')
print('Example: ', sum([SCORING_ONE[other][me] for other, me in matchdata('example')]))
print('Input:   ', sum([SCORING_ONE[other][me] for other, me in matchdata('input')]))
print()
print('# Part two # ')
print('Example: ', sum([SCORING_TWO[other][me] for other, me in matchdata('example')]))
print('Input:   ', sum([SCORING_TWO[other][me] for other, me in matchdata('input')]))

