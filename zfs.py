#!/usr/bin/python
#
##########################################################
# Stuart AH 9-7-18
# program to print zfs volumes and encryption status
##########################################################
#

import subprocess

def main():
    output = subprocess.check_output("zfs get encryption", shell=True)
    for line in output.splitlines():
        if "encryption  on" in line:
            print line


if __name__ == "__main__":
    main()

