"""Taxi Main"""
import sys

if __name__ == "__main__":
    test_data_file = sys.argv[1]
    with open(test_data_file, 'r') as file:
        line = file.readline()
        print(line)
