import sys
import math
import argparse

parser = argparse.ArgumentParser(
    description='Get the stats from a given column in a given file.')
parser.add_argument(
    '--file_name',
    type=str,
    help='The file to read')
parser.add_argument(
    '--col_num',
    type=int,
    help='The column to calculate stats for (starts at 0)')

args = parser.parse_args()

f = open(args.file_name, 'r')

V = []

for l in f:
    A = [int(x) for x in l.split()]
    V.append(A[args.col_num])

mean = sum(V)/len(V)

stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

print('mean:', mean)
print('stdev:', stdev)
