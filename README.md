README - AHMED SAHARDID
 Lab 8: Part 2 (Take-Home) Automating User Management
 INET4031 Add Users Script and User List
Overview
  This project automates user creation on a Linux system. It reads a list of usernames, passwords, and groups from an input file and creates all the users at once instead of doing it      manually. This saves time and reduces errors.

How It Works
  The program reads each line from the input file and uses Linux commands to create users, set passwords, and assign them to groups. It skips any lines that start with # and ignores       lines that don’t have the right number of fields.
  
Input File Format
  The input file lists users in this format:
  username:password:last:first:groups
  Each line represents one user. Lines starting with # are skipped, and using - means no group is added.

Command Execution
  Run the script with:
  sudo ./create-users.py < create-users.input
  The < sends the input file’s data into the program, which reads each line and creates users automatically.

Dry Run
  For testing, comment out all os.system() lines. The program will only print what it would do without making any real changes.
