#!/usr/bin/env python3

def calc_totals(filename):
    with open(filename) as f:
        elves = [map(int, i.split('\n')) for i in f.read().strip().split('\n\n')]
    return [sum(i) for i in elves]

if __name__ == '__main__':
    print('# Part one #')
    print('Example: ', max(calc_totals('example')))
    print('Input  : ', max(calc_totals('input')))
    print()
    print('# Part two #')
    print('Example: ', sum(sorted(calc_totals('example'), reverse=True)[:3]))
    print('Input  : ', sum(sorted(calc_totals('input'), reverse=True)[:3]))

