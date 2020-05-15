import os
import sys


def lower_case_all(dirname):
    for dir_path, dirs, files in os.walk(dirname, topdown=False):

        for filename in files:
            os.rename(os.path.join(dir_path, filename),
                      os.path.join(dir_path, filename.lower()))

        for dir_name in dirs:
            os.rename(os.path.join(dir_path, dir_name),
                      os.path.join(dir_path, dir_name.lower()))

    os.rename(dirname, dirname.lower())


if sys.argv[1]:
    lower_case_all(sys.argv[1])
else:
    print("Please pass the paths to check as parameters to the script")