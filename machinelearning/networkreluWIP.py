import numpy as np
from nodefunction import *

weightrandomizationfactor = 0.1
biasrandomizationfactor = 0.1

learningrate = 0.5

def initializedata(inputsize, neuronsize, layersize, outputsize):

    n2 = []
    inputs1 = np.zeros((1, inputsize), dtype = float)
    n2.append(inputs1)

    for a in range(0, layersize):
        neurons1 = np.zeros((1, neuronsize), dtype = float)
        n2.append(neurons1)

    outputs1 = np.zeros((1, outputsize), dtype = float)
    n2.append(outputs1)

    dn2 = n2.copy()
    a2 = n2.copy()

    b2 = [[0]]
    for a in range(1, len(n2)):
        b1 = (biasrandomizationfactor * np.random.rand(1, len(n2[a][0]))) - (biasrandomizationfactor / 2)
        b2.append(b1)

    db2 = [[0]]
    for a in range(1, len(n2)):
        db1 = np.zeros((1, len(n2[a][0])), dtype = float)
        db2.append(db1)

    w3 = [[[0]]]
    for a in range(1, len(n2)):
        w2 = (weightrandomizationfactor * np.random.rand(len(n2[a][0]), len(n2[a - 1][0]))) - (weightrandomizationfactor / 2)
        w3.append(w2)

    dw3 = [[[0]]]
    for a in range(1, len(n2)):
        dw2 = np.zeros((len(n2[a][0]), len(n2[a - 1][0])), dtype = float)
        dw3.append(dw2)

    return (a2, n2, b2, w3, dn2, db2, dw3)

#install kaiming initialization
#batch normalization
#weight decay / l2 regularization
#adaptive optimizers?





def runnetwork(input, dataset, targetoutput):

    [a2, n2, b2, w3, dn2, db2, dw3] = dataset #all the numbers shoot off to infinity for some reason and results in quick integer overflow
    #reexamine wtf is happening but also try smaller initial weight distribution

    n2[0] = input

    for a in range(1, len(n2)):
        a2[a] = np.matmul(w3[a], (n2[a - 1].T)).T #this is exceeding integer overflow somehow wtf????
        a2[a] = np.add(a2[a], b2[a])
        n2[a] = relu(a2[a])

    output = n2[len(n2) - 1]

    outputvalue = np.argmax(output[0])

    costfunction = output - targetoutput

    cost = 0
    for a in range(0, len(costfunction[0])):
        cost = cost + costfunction[0][a] ** 2

    for layer in range(len(n2) - 1, 0, -1):
        if layer == len(n2) - 1:
            dn2[layer] = 2 * (n2[len(n2) - 1] - targetoutput)
        else:
            dn2[layer] = (np.matmul(w3[layer + 1].T, (drelu(a2[layer + 1]) * dn2[layer + 1]).T)).T

        db2[layer] =  db2[layer] + drelu(a2[layer]) * dn2[layer]

        dw3[layer] = dw3[layer] + np.matmul((drelu(a2[layer]) * dn2[layer]).T, n2[layer - 1])

    dataset = [a2, n2, b2, w3, dn2, db2, dw3]

    return (outputvalue, output, cost, costfunction, dataset)



def adjustnetwork(batchsize, dataset):

    [a2, n2, b2, w3, dn2, db2, dw3] = dataset 

    for layer in range(1, len(n2)):
        b2[layer] = b2[layer] + np.clip((db2[layer] / batchsize), -5.0, 5.0) * learningrate
        w3[layer] = w3[layer] + np.clip((dw3[layer] / batchsize), -5.0, 5.0) * learningrate
        #print(np.amax(np.clip((dw3[layer] / batchsize), -5.0, 5.0) * learningrate))

    db2 = [[0]]
    dw3 = [[[0]]]

    for layer in range(1, len(n2)):
        db1 = np.zeros((1, len(n2[layer][0])), dtype = float)
        db2.append(db1)

        dw2 = np.zeros((len(n2[layer][0]), len(n2[layer - 1][0])), dtype = float)
        dw3.append(dw2)

    dataset = [a2, n2, b2, w3, dn2, db2, dw3]

    return dataset



def dryrunnetwork(input, dataset):

    [a2, n2, b2, w3, dn2, db2, dw3] = dataset

    n2[0] = input

    for a in range(1, len(n2)):
        a2[a] = np.matmul(w3[a], (n2[a - 1].T)).T
        a2[a] = np.add(a2[a], b2[a])
        n2[a] = relu(a2[a])

    output = sigmoid(n2[len(n2) - 1])

    outputvalue = np.argmax(output[0])

    return outputvalue