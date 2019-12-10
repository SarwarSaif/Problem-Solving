# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:23:48 2018

@author: majaa
"""

import sys

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    for i, v in enumerate(argv):
        print("argv[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    main(sys.argv[1:])

The mission
There is an arbitrary [string]. Please implement a function that should return the following,

"Hello [string]!"
For example, it should return "Hello World!" when the input is "World",
and should return "Hello track!" when the input is "track".

Implementation
CLI
Implement a command line application that accepts input.in file and output the results to stdout.
For details, see the "Command line application template" section at the bottom of the page.

Input Rules
Your CLI program should accept an input file: input.in

The input.in file's format is as below:

[string]
Output Rules
Your CLI program should return an output as stdout.

The output's format is as below:

Hello [string]!
Input & Output samples
Sample 1
$ ./myApp World
stdout

Hello World!
Sample 2
$ ./myApp track
stdout

Hello track!
There are other input & output samples defined in this file: test/basic_testcases.json
You can use it as a reference while working on this exercise.

Command line application template for Python3.x
Implement CLI application by editing main.py.
You may add new files to keep your code clean, if it is allowed in your challenge.

How to get input parameters
In main.py, there is a function called main, which gives command line arguments as argv.

def main(argv):
    # code to run
argv passed here is came from sys.argv. Script name information is excluded in argv of main method.

How to output result
You can use the standard print() method to output results to stdout.

print(result)
Install External Libraries
If you want to use external libraries, do the following:

Write the library name and version in requirements.txt
Example:
numpy==1.11.0
requests==2.12.4

track clone https://app.tracks.run/tutorial/exams/3d75643688e64779972f5ed9a85013e9/challenges/240

track pull