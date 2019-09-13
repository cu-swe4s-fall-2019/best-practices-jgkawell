# best-practices

## Description
This repository contains some demonstration code. The `style.py` is simply an example of how Python code should be structured to meet Pep8 style requirements. Also, `get_column_stats.py` performs some simple data analysis (mean and stdev) for a column on a given, tab-separated, integer data file. `basics_test.sh` performs some functional testing on these files.

## How to use
The column stats program takes in a file name and column number to parse. Your command to run the file should take the following form:

```
python get_column_stats.py --file_name {your_file_name} --col_num {your_column_number}
```

You can also run the functional tests with the simple command:

```
./basics_test.sh
```

## Installation
The project only requires cloning the repository and making sure that you have Python installed. In order to run the functional testing, you'll have to also have installed `pycodestyle` through pip and you need to make the testing script executable:

```
pip install pycodestyle
chmod +x basics_test.sh
```
