import numpy as np
#input 
X=np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
#print(x)
#desired outputs
d=np.array([-1,-1,-1,1])

class Neuron:
    def __init__(self,neuron_input):
        self.neuron_input = neuron_input
    def operate(self):
        inp = self.neuron_input
        



n1 = Neuron(3)
print(n1.neuron_input)


class Layer:
    def __init__(self,neuron_num):
        self.neuron_num = neuron_num



l1 = Layer(2)
print(l1.neuron_num)

