import csv
import subprocess
import sys


def main():
    """Generate ABC/HR files (data is in an CSV)"""

    # check command line for arguments
    if len(sys.argv) != 2:
        print ('usage: {:} <CSV with test data>'.format(sys.argv[0]))
        exit(1)

    # record command line args
    file_with_test_data = sys.argv[1]

    with open(file_with_test_data, newline='') as test_description:
        csvreader = csv.DictReader(test_description, delimiter=';', quotechar='"')
        for z in csvreader:
            print(z['CmdOriginal'])
            print(z['CmdHR'])
            print(z['CmdTested'])

if __name__ == '__main__':
    main()
