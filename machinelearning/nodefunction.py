import numpy as np



def sigmoid(array):
    
    return 1 / (1 + np.exp(-array))



def dsigmoid(array): 
    
    x = 1 / (1 + np.exp(-array))

    return (x * (1 - x))


def sigmoidtodsigmoid(array): #using this still is the fastest
    #need to use sigmoid to dsigmoid as node values are already sigmoided
    return (array * (1 - array))


def relu(array):
    
    return np.maximum(0.1 * array, array)


def drelu(array):

    return 1.1 * (array > 0) - 0.1


def relutodrelu(array):

    return 1.1 * (array > 0) - 0.1