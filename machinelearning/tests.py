import random
import numpy as np
import json

def initializedataset(filename):
    print("Loading data")

    with open(filename, "r") as openfile:
        datafile = json.load(openfile)

    length = len(datafile)

    print("Loaded", length, "test cases")

    random.shuffle(datafile)

    global testfile
    testfile = datafile[:round(length / 2)]
    global accuracyfile
    accuracyfile = datafile[round(length / 2):]

def writtennumbertestset(batchsize):
    testset = testfile

    random.shuffle(testset)

    returnarray = []
    for a in range(0, batchsize):
        input = testset[a][0]
        output = testset[a][1]

        returnarray.append([np.array([input]), np.array([output])])

    return returnarray

def writtennumberaccuracyset(batchsize):
    testset = accuracyfile

    random.shuffle(testset)

    returnarray = []
    for a in range(0, batchsize):
        input = testset[a][0]
        output = testset[a][1]

        returnarray.append([np.array([input]), np.array([output])])

    return returnarray