#!/usr/bin/env python3
"""RZFeeser@alta3.com | Alta3 Research
   Using the CSV library to work with CSV data."""

# standard library import
#import csv
import os

while True:
    num= int(input("Enter 1 to manually create rcfile or 2 to use csv_users file:  "))
    if num == 1:
        os.system("python3 openstackrc_maker.py")
        break
    elif num == 2:
        os.system("python3 rclooper.py")
        break
    else:
        print("Enter input option 1 or 2. Try again.")


