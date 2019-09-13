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

try:
    f = open(args.file_name, 'r')
except FileNotFoundError:
    sys.stderr.write("ERROR: File not found. Try a different file name.")
    sys.exit(1)


V = []

for l in f:
    try:
        A = [int(x) for x in l.split()]
        V.append(A[args.col_num])
    except ValueError:
        sys.stderr.write("ERROR: Bad value. Only works on integer values.")
        sys.exit(1)
    except IndexError:
        sys.stderr.write(
            "ERROR: Index out of range. Try a different column number.")
        sys.exit(1)

mean = sum(V)/len(V)

stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

print('mean:', mean)
print('stdev:', stdev)
