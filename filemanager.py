#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""filemanager.py

The file contains the main program and the program logic.
"""

from io import TextIOWrapper
import os
import shutil

def read() -> None:
    path: str = input("Enter the file path to read: ")
    file: str = open(path, "r", encoding="utf-8")
    print(file.read())
    input("Please enter...")
    file.close()
    return None

def write() -> None:
    path: str = input("Enter the path of file to write ir create: ")
    if os.pathisfile(path):
        print("Rebuilding the existing file")
    else:
        print("Creating new file")
    text: str = input("Enter text: ")
    file: TextIOWrapper = open(path, "w", encoding="utf-8")
    file.write(text)
    return None

def add() -> None:
    path: str = input("Enter the filepath:")
    text: str = input("Etner text to add")
    file: TextIOWrapper =  open(path, "a")
    file.write("\n"+text)
    return None

def delete() -> None:
    path: str = input("Enter the path of the file deletion:")
    if os.path.exists(path):
        print("File found")
        os.remove(path)
        print("File has been deleted")
    else:
        print("File does not exist")
    return None

def dir_list() -> None:
    path: str = input("Enter the directory pathj to display:")
    sortlist: list[str] = sorted(os.listdir(path))
    i = 0
    while(i < len(sortlist)):
        print(sortlist[i]+"\n")
        i += 1
    return None

def check() -> None:
    fp = int(input("Check existence of \n1.File \n2. Directory\n"))
    if fp == 1:
        path: str = input("Enter the filepath:")
        os.path.isfile(path)
        if os.path.isfile(path) == True:
            print("File found")
        else:
            print("File not found")
    if fp == 2:
        path: str = input("Enter te directory path:")
        os.path.isdir(path)
        if os.pathisdir(path) == False:
            print("Directory found")
        else:
            print("Directory not found")
    return None

def move() -> None:
    path1: str = input("Enter the source path of file to move:")
    mr: int = int(input("1.Rename \n2. Move \n"))
    if mr == 1:
        path2: str = input("Enter the destination path and filename")
        shutil.move(path1, path2)
        print("File renamed")
    if mr == 2:
        path2: str = input("Enter the destination path and filename")
        shutil.move(path1, path2)
        print("File moved")
    return None        

def copy() -> None:
    path1: str = input("Enter the path of the file to copy or rename.")
    path2: str = input("Enter the path to copy:")
    shutil.copy(path1, path2)
    print("File copied")
    return None

def make_dir() -> None:
    path: str = input("Enter the directory name with path to make \neg. C:\\Hello\\Newdir \nWhere Newdir is new directory: ")
    os.makedirs(path)
    print("Directory created")
    return None

def remove_dir() -> None:
    path: str = input("Enter the path of Directory: ")
    tree_dir: int = int(input("1.Deleted Directory \n2 Delete directory tree \n3.Exit"))
    if tree_dir == 1:
        os.rmdir(path)
    if tree_dir == 2:
        shutil.rmtree(path)
    if tree_dir == 3:
        exit()
    return None

def open_file() -> None:
    path: str = input("Enter the path of program:")
    try:
        os.startfile(path)
    except:
        print("File not found")
    return None

run: int = 1
while(run == 1):
    try:
        os.system("clear")
    except OSError:
        os.system("cls")
    print()
    print()
    print()
    dec: int = int(input("""1.Read a file
2.Write to a file
3.Append text to a file
4.Delete a file
5.List files in a directory
6.Check file existence
7.Move a file
8.Copy a file
9.Copy a file
10.Delete a directory
11.Open a program
12.Exit

"""))

    if dec == 1:
        read()
    if dec == 2:
        write()
    if dec == 3:
        add()
    if dec == 4:
        delete()
    if dec == 5:
        dir_list()
    if dec == 6:
        check()
    if dec == 7:
        move()
    if dec == 8:
        copy()
    if dec == 9:
        make_dir()
    if dec == 10:
        open_file()
    if dec == 11:
        exit()
    run = int(input("1.return to menu\n2.Exit \n"))
    if run == 2:
        exit()
