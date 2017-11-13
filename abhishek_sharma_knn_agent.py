'''
Developer: Abhishek Manoj Sharma
Date: September 9, 2017
Class: Agent
'''

from operator import itemgetter
from collections import Counter


'''
Agent Class
Methods:
1. sensor()
2. agentFunction()
3. actuator()
4. calcEuclidean()
The 4 methods interact with each other and return a prediction to the environment based on the percept received.
'''
class Agent:
    '''
    The sensor() method accepts k, training file, and percept sequence from environment and passes
    them to the agentfunction() method.
    It returns a prediction from the obtained by agentFunction() and actuator() and passes it back to the environment.
    '''
    def sensor(self,k,training_file,percept):
        del percept[len(percept) - 1]
        map(float, percept)
        prediction = self.agentFunction(k,training_file,percept)
        return prediction

    '''
    The agentFunction() method accepts k, training file, percept from the sensor and calculates the Euclidean distance
    using the calcEucliden() method. It then sorts the lookup_table based on the distances calculated and passes
    the value of k, sorted lookup table, and number of inputs to the actuator() method.
    '''
    def agentFunction(self,k,training_file,percept):
        with open(training_file) as trainer:
            for line in trainer:
                if "@inputs" in line:
                    input_count = 1
                    input_count = input_count + line.count(",")
                if "@data" in line:
                    lookup_table = []
                    for line in trainer:
                        lookup_table.append(line.strip().split(","))
        count = len(lookup_table)-1
        while count >= 0:
            euclidean_distance = self.calcEuclidean(percept,lookup_table[count])
            lookup_table[count].append(euclidean_distance)
            count-=1
        lookup_table = sorted(lookup_table, key=itemgetter(input_count + 1))
        prediction = self.actuator(k,lookup_table,input_count)
        return prediction

    '''
    Based on the value of k and the values with least distance, the actuator() method classifies the percepts and 
    assignments them the most likely value.
    It then returns it prediction to agentFunction(), which returns the prediction to sensor(), and sensor() returns
    the prediction back to the Environment.
    '''
    def actuator(self,k,lookup_table,input_count):
        predicted_values=[]
        curr_k = -1
        prediction = []
        while curr_k<int(k):
            curr_k = curr_k + 2
            for j in range (0,int(curr_k)):
                predicted_values.append(lookup_table[j][input_count])
            prediction.append(Counter(predicted_values).most_common()[0][0])
        return prediction

    '''
    The calcEuclidean() method accepts the percept and lookup value to calculate the distance between them.
    It returns the Euclidean distance between them as a float data type.
    '''
    def calcEuclidean(self,percept,lookup_value):
        euclidean_distance = 0.00;
        count = len(percept)-1
        while count>=0:
            f1 = float(percept[count])
            f2 = float(lookup_value[count])
            euclidean_distance = euclidean_distance + (f1-f2)**2
            count-=1
        return euclidean_distance
