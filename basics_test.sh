# Check code styling for all python files
pycodestyle style.py
pycodestyle get_column_stats.py

# Download and setup ssshtest
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Simple test with random ints
(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run random_test python get_column_stats.py --file_name data.txt --col_num 2
assert_no_stderr
assert_exit_code 0

# Simple test with all 1s
V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run basic_test python get_column_stats.py --file_name data.txt --col_num 1
assert_in_stdout "mean: 1.0"
assert_in_stdout "stdev: 0.0"
assert_no_stderr
assert_exit_code 0

# Testing index error
V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run index_error_test python get_column_stats.py --file_name data.txt --col_num 10
assert_stderr
assert_in_stderr "Index out of range"
assert_exit_code 1


# Testing erroring out due to doubles
V=0.5
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run doubles_test python get_column_stats.py --file_name data.txt --col_num 1
assert_stderr
assert_in_stderr "Bad value"
assert_exit_code 1

# Testing erroring out due to no file
run no_file_test python get_column_stats.py --file_name no_file.txt --col_num 1
assert_stderr
assert_in_stderr "File not found"
assert_exit_code 1
