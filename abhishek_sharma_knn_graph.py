'''
Developer: Abhishek Manoj Sharma
Date: September 9, 2017
Class: Graph
'''

#Code Snippets for graph plot taken from https://matplotlib.org/

import matplotlib.pyplot as plot

'''
Graph class:
This class receives accuracy values and directory name from class Environment.
The plotGraph() method then plots a graph using the matplotlib library.
'''
class Graph:
    def plotGraph(self, accuracy_values, name):
		#Creating k_list to store the values of k
        k_list = []
        for i in range(1, len(accuracy_values)*2, 2):
            k_list.append(i)
		
		#plot() method is used to define the values and the type of graph
        plot.plot(k_list, accuracy_values, '-o')
		
		#Setting the labels for X and Y axes and the graph title
        plot.xlabel("Value of K")
        plot.ylabel(("Accuracy (%)"))
        plot.title("Dataset: " + name)
		
		#Setting up the window name that will display the graph
        plot.gcf().canvas.set_window_title(name+": Line Graph - Accuracy vs Values of K") #Credits: Solution posted by user'itoed' on https://github.com/jupyter/notebook/issues/919
        plot.show()
