import random
import turtle as t
import json

import drawinginput
import displaychunkedarray
import imagemodifier

canvassize = 900
pensize = 75
chunks = 30

copiespernumber = 50

dataset = []

xyarraylist = []

for number in range(0, 10):

    targetoutput = []
    for a in range(0, 10):
        if a == number:
            targetoutput.append(1)
        else:
            targetoutput.append(0)

    for copy in range(0, copiespernumber):
        title = str(number)

        drawinginput.drawinginput(canvassize, pensize, title)

        xyarraylist.append([imagemodifier.imagetoxyarray("data/temp.ps"), targetoutput])

with open("data/rawdata.json", "w") as outfile:
    json.dump(xyarraylist, outfile)

for z in range(0, len(xyarraylist)):
    xyarray = xyarraylist[z][0]
    for a in range(0, 5):
        if a == 0:
            array = xyarray
        else: #skew is not included do smth with skew later
            maxangle = 20
            angle = random.random() * maxangle * 2
            
            array = imagemodifier.rotate(angle - maxangle, xyarray)

        borders = imagemodifier.getborder(array)

        shiftarrayx = [(random.random() ** 2) * borders[0], (random.random() ** 2) * borders[0], 0, (random.random() ** 2) * borders[1], (random.random() ** 2) * borders[1]]
        shiftarrayy = [(random.random() ** 2) * borders[2], (random.random() ** 2) * borders[2], 0, (random.random() ** 2) * borders[3], (random.random() ** 2) * borders[3]]

        for b in range(0, len(shiftarrayx)):
            for c in range(0, len(shiftarrayy)):
                outputarray = (imagemodifier.shifty(round(shiftarrayy[c]), imagemodifier.shiftx(round(shiftarrayx[b]), array))).copy()
                
                dataset.append([imagemodifier.xyarraytoarray(imagemodifier.xyarraychunker(chunks, outputarray)), xyarraylist[z][1]])
                #displaychunkedarray.displaychunkedarray(canvassize, chunks, dataset[len(dataset) - 1][0]) #if you want to display what the machine sees

                print(len(dataset))

with open("data/data.json", "w") as outfile:
    json.dump(dataset, outfile) 