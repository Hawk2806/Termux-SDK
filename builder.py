#!/usr/bin/env python
import os

print("Termux SDK Builder")
print("Select a Name and Folder and Type of Project")
name = input("New Project Name: ")
project_dir = input("Project Folder: ")
print("Type of Project")
print("(1) Termux C Application")
print("(2) Termux C++ Application")
print("(3) Python Application")

project_type = input("Select Project Type: ")

if project_type == "1":
    createproject(name,project_dir,"C")
elif project_type == "2":
    createproject(name,project_dir,"CXX")
elif project_type == "3":
    createproject(name,project_dir,"PYTHON")
else:
    print("Invalid Project Type")

def createproject(arg1,arg2,arg3):
    if arg3 == "PYTHON":
        os.system("~/.sdkfiles/buildscripts/createpythonproject.sh {0} {1}".format(arg2,arg1))
    elif arg3 == "CXX":
        os.system("~/.sdkfiles/buildscripts/createcxxproject.sh {0} {1}".format(arg2,arg1))
    elif arg3 == "C":
        os.system("~/.sdkfiles/buildscripts/createcproject.sh {0} {1}".format(arg2,arg1))
    else:
        pass