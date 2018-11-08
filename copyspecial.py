#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


"""
Assignment: CopySpecial

Description: program that takes in a directory to find special files.
Shows the absolute path to the files and then prints them to the stdout.
Two options are allowed. --tozip and --todir.
--todir copies special files to directory specified
--tozip runs command to zip files and zips them there

Author: Aaron Jackson
Github: TimeApollo
"""
__author__ = 'TimeApollo'

import sys
import re
import os
import shutil
import commands
import argparse

"""Copy Special exercise"""


def zip_to(paths, zippath):
    """given file paths and a zippath name, zips files"""

    cmd = 'zip -j ' + zippath
    for path in paths:
        cmd += ' ' + path

    print("Command I'm going to do: " + cmd)

    (status, output) = commands.getstatusoutput(cmd)

    if status:
        print(output)
        sys.exit(status)


def copy_to(paths, dir):
    """given list of paths, copies files into given directory"""
    for path in paths:
        shutil.copy(path, dir)


def get_special_paths(dir):
    """returns list of ablsolute paths of special files in given directory"""
    return [shutil.abspath(file)
            for file in os.listdir(dir)
            if re.search(r'\_\_\w+\_\_', file)]


# +++your code here+++
# Write functions and modify main() to call them code

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory to look for special files')

    args = parser.parse_args()

    # Parsing command line arguments is a must-have skill. This is
    # input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    paths = get_special_paths(args.from_dir)

    if args.todir:
        copy_to(paths, args.todir)
    elif args.tozip:
        zip_to(paths, args.tozip)
    else:
        for path in paths:
            print(path)


if __name__ == "__main__":
    main()
