import numpy as np
# input
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
# print(x)
# desired outputs
d = np.array([-1, -1, -1, 1])
#input weigths
np.random.seed()
w = np.random.rand(1,3)
c=0.1

class Neuron:
    def __init__(self, ):
      pass

    def get_values(self,neuron_input, weights,d):
        self.neuron_input = neuron_input
        self.weights = weights
        self.d = d
        self.ls = 0

    def forward(self):
        # forward propogation
        net = np.matmul(self.weights, self.neuron_input)
        #print("Net =",net)
        o = self.activation(net)
        self.ls = self.learning_signal(o)
        

    def activation(self, net):
        # Signum Activation function
        return 1 if net > 0 else -1
    
    def learning_signal(self,out):
        ls = 0.5*c*(d-out)*self.neuron_input
        return(ls)


x=X[1]
d=d[1]
n1 = Neuron()
n1.get_values(x,w,d)
print(n1.forward())


class Layer:
    def __init__(self, neuron_num):
        self.neuron_num = neuron_num
        self.neuron=[]
        for i in range(neuron_num):
            self.neuron.append(Neuron())
    

l1 = Layer(2)
print(l1.neuron_num)
