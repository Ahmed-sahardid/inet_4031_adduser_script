#!/usr/bin/python3

# INET4031
# Author: Ahmed Sahardid
# Date Created: Oct 27, 2025
# Last Modified: Oct 27, 2025

# lets me run linux cmds (os), use regex (re), and read files (sys)
import os
import re
import sys

def main():
    # read each line from the input file
    for line in sys.stdin:

        # skip lines that start with #
        match = re.match("^#", line)

        # split line by :
        fields = line.strip().split(':')

        # skip bad or commented lines
        if match or len(fields) != 5:
            continue

        # get user info
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # handle multiple groups
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % (username))
        # add user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        # print(cmd)
        # os.system(cmd)

        print("==> Setting the password for %s..." % (username))
        # set password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        # print(cmd)
        # os.system(cmd)

        # add to groups if needed
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print(cmd)
                # os.system(cmd)

if __name__ == '__main__':
    main()

