from networkreluWIP import *

from tests import *

import drawinginput
import imagemodifier

layersize = 32
layernumber = 4

datasetname = "data/data62500.json"
initializedataset(datasetname)
batchsize = 300 #must be less than total dataset length
iterationlength = 10000

canvassize = 900
pensize = 75
numberofchunks = 30



testset = writtennumbertestset(1) #dry testrun to find input and outputs
inputsize = len(testset[0][0][0])
outputsize = len(testset[0][1][0])

dataset = initializedata(inputsize, layersize, layernumber, outputsize) 

for a in range(0, iterationlength):#maybe make it move the drawn image around and dry run and take the average value number
    testset = writtennumbertestset(batchsize)
    accuracyset = writtennumberaccuracyset(batchsize)

    averagecost = 0
    correctvalues = 0
    for test in range(0, batchsize):
        [outputvalue, output, cost, costfunction, dataset] = runnetwork(testset[test][0], dataset, testset[test][1])
        
        averagecost = averagecost + cost

        if np.argmax(accuracyset[test][1][0]) == dryrunnetwork(accuracyset[test][0], dataset):
            correctvalues = correctvalues + 1

    averagecost = averagecost / batchsize
    batchaccuracy = correctvalues / batchsize
    print("Average cost for batch", a, "is", round(averagecost, 2), "and accuracy is", round(batchaccuracy, 2))

    dataset = adjustnetwork(batchsize, dataset)



while True:
    drawinginput.drawinginput(canvassize, pensize, "Write a number")

    inputarray = np.array(imagemodifier.xyarraytoarray(imagemodifier.xyarraychunker(numberofchunks, imagemodifier.imagetoxyarray("data/temp.ps"))))

    print("The network guesses (", dryrunnetwork(inputarray, dataset), ")")