# define file input/output functions here
import os

def file_exists(path):
    return os.path.isfile(path)

def get_lines_for_file(path):
    f = open(path, "r")
    return f.readlines()

def write_lines_for_file(path, lines):
    f = open(path, "w")
    f.writelines(lines)