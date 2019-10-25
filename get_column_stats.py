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


def get_values(f, col_num):
    values = []
    for l in f:
        array = [int(x) for x in l.split()]
        values.append(array[col_num])

    return values


def get_mean(values):
    return sum(values) / len(values)


def get_stdev(values):
    mean = get_mean(values)
    return math.sqrt(sum([(mean-x)**2 for x in values]) / len(values))


def print_results(mean, stdev):
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
        values = get_values(f, args.col_num)
    except ValueError:
        sys.stderr.write(
            "ERROR: Bad value. Only works on integer values.\n")
        sys.exit(1)
    except IndexError:
        sys.stderr.write(
            "ERROR: Index out of range. Try a different column number.\n")
        sys.exit(1)

    try:
        mean = get_mean(values)
        stdev = get_stdev(values)
    except ZeroDivisionError:
        sys.stderr.write(
            "ERROR: Division by zero. Is the data blank?\n")
        sys.exit(1)

    print_results(mean, stdev)
