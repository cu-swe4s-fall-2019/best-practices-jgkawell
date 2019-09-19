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


def getValues(f, col_num):
    V = []
    for l in f:
        A = [int(x) for x in l.split()]
        V.append(A[col_num])

    return V


def getMean(V):
    return sum(V) / len(V)


def getStDev(V):
    mean = getMean(V)
    return math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))


def printResults(mean, stdev):
    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == "__main__":

    args = parser.parse_args()

    try:
        f = open(args.file_name, 'r')
    except FileNotFoundError:
        sys.stderr.write("ERROR: File not found. Try a different file name.\n")
        sys.exit(1)

    try:
        V = getValues(f, args.col_num)
    except ValueError:
        sys.stderr.write(
            "ERROR: Bad value. Only works on integer values.\n")
        sys.exit(1)
    except IndexError:
        sys.stderr.write(
            "ERROR: Index out of range. Try a different column number.\n")
        sys.exit(1)

    try:
        mean = getMean(V)
        stdev = getStDev(V)
    except ZeroDivisionError:
        sys.stderr.write(
            "ERROR: Division by zero. Is the data blank?\n")
        sys.exit(1)

    printResults(mean, stdev)
