#!/usr/bin/env python3
import string

def rucksacks(filename):
    with open(filename) as f:
        for line in f.readlines():
            yield line.strip()

def split(item):
    return item[:len(item)//2], item[len(item)//2:]

def per_three(items):
    while True:
        try:
            yield [next(items), next(items), next(items)]
        except StopIteration:
            return

def find_dupl(items):
    return ''.join(set.intersection(*[set(item) for item in items]))

scoring = {}
scoring.update(zip(string.ascii_lowercase, range(1,27)))
scoring.update(zip(string.ascii_uppercase, range(27,53)))

print('# Part 1 #')
print('Example: ', sum([scoring[find_dupl(split(sack))] for sack in rucksacks('example')]))
print('Input:   ', sum([scoring[find_dupl(split(sack))] for sack in rucksacks('input')]))
print()
print('# Part 2 #')
print('Example: ', sum([scoring[find_dupl(sacks)] for sacks in per_three((rucksacks('example')))]))
print('Input:   ', sum([scoring[find_dupl(sacks)] for sacks in per_three((rucksacks('input')))]))
