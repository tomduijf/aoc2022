#!/usr/bin/env python3
'''
Solution to: https://adventofcode.com/2022/day/4
'''

def assignments(filename):
    def to_range(assignment):
        a,b = assignment.split('-')
        return range(int(a),int(b)+1)

    with open(filename) as f:
        for line in f.readlines():
            a,b = line.strip().split(',')
            yield to_range(a), to_range(b)

def count_sets(assignments, test):
    count = 0
    for a, b in assignments:
        count += 1 if test(a, b) else 0
    return count

def test_contains_fully(a,b):
    return bool(set(a).issubset(b) or set(b).issubset(a))

def test_contains_partially(a,b):
    return bool(set(a).intersection(b))


print('# Part one #')
print('Example: ', count_sets(assignments('example'), test_contains_fully))
print('Input:   ', count_sets(assignments('input'), test_contains_fully))
print()
print('# Part two #')
print('Example: ', count_sets(assignments('example'), test_contains_partially))
print('Input:   ', count_sets(assignments('input'), test_contains_partially))

