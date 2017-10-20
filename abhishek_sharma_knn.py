'''
Developer: Abhishek Manoj Sharma
Class: CS 256 Section 2
Assignment 1: (KNN Algorithm)
Date: September 9, 2017
Inputs (from command line):
1. Directory containing data files
2. Value of k
'''

import sys
import os
from abhishek_sharma_knn_environment import Environment

#checks if k is even
if int(sys.argv[2])%2==0:
    print "Value of k should be odd.\nExiting program."
	
#checks if directory path is valid, if yes, then creates an object of class Environment and calls the sendToAgent() method
elif os.path.isdir(sys.argv[1]):
    e = Environment()
    e.sendToAgent(sys.argv[1],sys.argv[2])
	
#exits the program if directory name is invalid
else:
    print sys.argv[1],"directory not found.\nExiting program."