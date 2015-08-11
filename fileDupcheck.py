#!/usr/bin/python
'''Script will iterate through multiple directories with a parent directory
to check the duplication of data(file) and remove duplicate files'''
import os
import hashlib
import sys


dirname = sys.argv[1]
os.chdir(dirname)
duplicate = set()
'''Created a function that will check duplication of file using hashlib inbuilt function''' 
def dup_fileremove(dir):
    os.chdir(dir)
    path=os.getcwd()
    print ("The dir is: ", path)
    for filename in os.listdir(dir):
        filehash = None
        filepath=os.path.join(dir, filename)
        print("Current file path is: ", filepath)
        if os.path.isdir(filepath):
            dup_fileremove(filepath)
        elif os.path.isfile(filepath):
            filehash =hashlib.md5(file(filepath).read()).hexdigest()
        if filehash is not None and filehash not in duplicate:
            duplicate.add(filehash)
        elif filehash is not None:
            os.remove(filepath)
            print("removed : ", filepath)

dup_fileremove(dirname)
