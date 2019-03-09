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

    # Fields that we will use as shell commands
    flds_cmds=['CmdOriginal', 'CmdHR', 'CmdTested']

    with open(file_with_test_data, newline='') as test_description:
        csvreader = csv.DictReader(test_description, delimiter=';', quotechar='"')
        for row in csvreader:
            for cmd in flds_cmds:
                if subprocess.call(row[cmd], shell=True) != 0:
                    print('FAILED at converting for Test {:}, running {:} ({:})'.format(row['Test number'], cmd, row[cmd]))
        print('FINISHED')

if __name__ == '__main__':
    main()
