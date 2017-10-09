#!/usr/bin/env python

"""
Utility for cleaning files, applying Pylint ve Pep8 to the package.

This is not part of your package.
It can be safely deleted.

Requirements:
    pylint and pep8 should be on path.
If you don't have them, install them by the following commands:
    pip install pylint pep8
"""

import os
import fnmatch


def get_list_of_py_files(topdir=None):
    """
    Returns the list of .py files as a list.
    """
    if topdir is None:
        topdir = os.path.dirname(os.path.abspath(__file__))
        # print(topdir)

    file_list = []
    for root, dirs, files in os.walk(topdir,  # pylint: disable=W0612
                                     topdown=False):
        for name in files:
            full_file_path = os.path.join(root, name)
            if fnmatch.fnmatch(full_file_path, "*.py"):
                if not fnmatch.fnmatch(full_file_path, "*.eggs*"):
                    # ignore .py files in .eggs folders.
                    file_list.append(full_file_path)
        # for name in dirs:
        #     print(os.path.join(root, name))
    # print(file_list)
    return file_list


def apply_pylint(file_list):
    """
    Applies pylint to all .py files in the package.
    """
    for file_path in file_list:
        cmd = "pylint " + '"' + file_path + '"'
        os.system(cmd)


def apply_pep8(file_list):
    """
    Applies pep8 to all .py files in the package.
    """
    for file_path in file_list:
        cmd = "pep8 " + '"' + file_path + '"'
        os.system(cmd)


def main():
    """
    Entry point of the module.
    """
    file_list = get_list_of_py_files()
    apply_pylint(file_list=file_list)
    apply_pep8(file_list=file_list)


if __name__ == "__main__":
    main()
