# Author: Hakan Bozkurt (27.03.2020)
# Algoritm: Single layer single neuron Perceptron (Ref. Zurada, Jacek M. "Artificial Neural Systems." New Yrok: W est Publishing Co 1 (1995): 992.)
# Case: AND Operation Using Perceptron Algorithm
# Perceptron network consist of one single neuron. There are 3 inputs, one of the inputs is the bias.

import numpy as np
import matplotlib.pyplot as plt

#input values of AND operation
X=np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
#print(x)
data_len = len(X)
#desired outputs
d=np.array([-1,-1,-1,1])

#input weigths
np.random.seed()
w = np.random.rand(1,3)

#Constant c
c=0.35

#Cycle error
Err = 0
iteration_num = 100
for j in range(iteration_num):
    i=0
    for x in X:
        #print("x =",x, "w= ",w)
        #Calculate the Net value
        net = np.matmul(w,x)
        #print("Net =",net)
        #Signum Activation function
        o = 1 if net>0 else -1
        print("out =", o, "d =",d[i])
        ls = 0.5*c*(d[i]-o)*x
        #print("learning signal =",ls)
        w = w + ls
        #print("new w =",w)
        Err = Err + 0.5*pow((d[i]-o),2)
        print("Error =",Err)
        i = (i+1)%data_len
       # print("i",i)
    #print("j =",j)

    #Iterations continue until cycle error become 0
    if Err > 0:
        Err = 0
    else:
        print("----------Training is completed---------")
        print("Final w values =",w)
        break
        
#Graphic Drawing
discriminant_x = np.arange(-0.1,1.2,0.1)
discriminant_y = (-1*w[0,2]-w[0,0]*discriminant_x)/w[0,1]

#Draws 0-1 categories as circles
px = [0,0,1]
py = [0,1,0]

plt.plot(px,py,'ro')
plt.plot(1,1,'bo')

#Draws discriminant using w weights
plt.plot(discriminant_x,discriminant_y)

plt.grid(True)
plt.axis([-0.1,1.1,-0.1,1.1])
plt.show()

