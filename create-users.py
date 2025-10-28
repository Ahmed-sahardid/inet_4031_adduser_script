#!/usr/bin/python3

# INET4031
# Author: Ahmed Sahardid
# Date Created: Oct 27, 2025
# Last Modified: Oct 27, 2025

# lets me run Linux commands (os), use regex to skip comments (re), and read input lines (sys)
import os
import re
import sys

def main():
    for line in sys.stdin:
        # skip lines starting with #
        match = re.match("^#", line)

        # split each line by :
        fields = line.strip().split(':')

        # skip bad or incomplete lines (not 5 fields)
        if match or len(fields) != 5:
            continue

        # get user info for username, password, and full name
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # split groups by commas if multiple exist
        groups = fields[4].split(',')

        # create user account
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)

        # set password for the new user
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd)

        # add user to listed groups
        for group in groups:
            if group != '-':  # skip if no group
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

if __name__ == '__main__':
    main()

