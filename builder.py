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
    os.system("~/.sdkfiles/buildscripts/createcproject.sh {0} {1}".format(project_dir,name))
elif project_type == "2":
    os.system("~/.sdkfiles/buildscripts/createcxxproject.sh {0} {1}".format(project_dir,name))
elif project_type == "3":
    os.system("~/.sdkfiles/buildscripts/createpythonproject.sh {0} {1}".format(project_dir,name))
else:
    print("Invalid Project Type")