#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 12:59:41 2021

@author: sazamore

Read-Write File
(for longterm game data)

This code is useful for adding a high score, resuming games where
left off, or recognizing if the code has been run before.

1. Check to see if a file exists. If it doesn't, make a new file & open it.
2. Save data to that file & close it. Recommended: each data point has its own line
3. Check to see if a file exists. If it does, then read it and save each line to an element in a list.

Notes: 
    1. YOU CAN IMPORT THIS SCRIPT!
        import rwFile
        rw.File.checkFile()
        
    2. This script will create a file on your computer! You may run
into access request prompts when you run this file. Accept to run
without error.

Modified from:
    https://www.guru99.com/reading-and-writing-files-in-python.html
    https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

"""
def checkFile(filename):
    '''Checks to see if the file exists. Filename can also be a path. 
    Returns boolean value:
        If it exists, a True is returned
        Otherwise, a False is returned'''
    try:
        file = open(filename,'r')
        file.close()
        return True
    except:
        return False

def write(data, filename='test.txt'):
    '''Opens a file to write and save data. This function will create a file 
    if it doesn't exist and overwrite it if it does.
    Arguments:
        data (list, int, float, str) - the  information that will be stored long term
        filename (optional,str) - the name of the file to add on to or create. Filename can also be a path.'''
    file = open(filename,"w+") # open a file with the write (w) format.
    
    if type(data)==list:
        # the data is a list
        for i in range(len(data)):
            file.write(str(data[i]) + '\r\n') # turn data into a string, save to a line and move to next line with '\n'
    else:
        # just one data point to save...
        file.write(str(data) + '\n') # turn data into a string, save to a line and move to next line with '\n'

    file.close()
    
def append(data,filename='test.txt'):
    '''Opens a file that already extists and adds data to it.
    Each new piece of data is added on a new line.
    Arguments:
        data (list, int, float, str) - the  information that will be stored long term
        filename (optional,str) - the name of the file to add on to or create. Filename can also be a path.'''
    file = open(filename,  "a")
    
    if type(data)==list:
        # the data is a list
        for i in range(len(data)):
            file.write(str(data[i]) + '\r\n') # turn data into a string, save to a line and move to next line with '\n'
    else:
        # just one data point to save...
        file.write(str(data) + '\n') # turn data into a string, save to a line and move to next line with '\n'

    file.close()

    
def read(filename='test.txt'):
    '''Opens a file that already exists and reads it. 
        Each line is stored in a new element (index)in a list.
        Arguments:
            filename (optional,str) - the name of the file to read. Filename can also be a path.'''
    file = open(filename,  "r")
    data = [] # empty list

    for line in file:
        data.append(line.rstrip()) # save each line to list, while removing new line, spaces
    
    file.close()
    return data
        
        
if __name__ == "__main__":
    # a demo
    # RUN CODE TWICE.
    import turtle
    
    HiScoreFile = 'myfile.txt' # use extension!
    
    if checkFile(HiScoreFile):
        # There is a high score already!
        # Get data from file
        hiScore = read(HiScoreFile)
        
        # Display high score using turtle:
        turtle.up()
        for i in range(len(hiScore)):
            font = ('Helvetica neue', 24)
            # write all the high scores
            turtle.write(hiScore[i],font=font)
            turtle.forward(50)
            turtle.ht()
        turtle.done()
            
    else:
        # There is no high score yet!
        initials =  input("Enter your 2 initials. Example: AA  \n")
        # Protip: see textBox.py for on-screen typing!
        
        # Organize data (if not done already)
        data = [initials, 100]  # make list of data: initials & score value
        
        # Save data to file
        write(data, HiScoreFile)
        
        print('file saved!')
        
        
        
        