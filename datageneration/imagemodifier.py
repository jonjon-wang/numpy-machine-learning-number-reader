from PIL import Image
import numpy as np
import math

def imagetoxyarray(imagename): #make a way to convert image to array
    img = Image.open(imagename)

    width, height = img.size

    imagearray = np.zeros(shape = (width, height), dtype = float)
    for x in range(0, width):
        for y in range(0, height):
            pixelavgvalue = (img.getpixel((x, y))[0] + img.getpixel((x, y))[0] + img.getpixel((x, y))[0]) / (3 * 255)
            imagearray[x][y] = 1 - pixelavgvalue

    return imagearray



def xyarraychunker(chunk, xyarray):
    width = len(xyarray)
    height = len(xyarray[0])

    processedvalue = np.zeros(shape = (chunk, chunk), dtype = float)

    chunksizex = width / chunk
    chunksizey = height / chunk

    for x in range(0, chunk):
        for y in range(0, chunk):
            sectorsize = 0
            for xchunk in range(round(chunksizex * x), round(chunksizex * (x + 1))):
                for ychunk in range(round(chunksizey * y), round(chunksizey * (y + 1))):
                    sectorsize = sectorsize + 1
                    processedvalue[x][y] = processedvalue[x][y] + xyarray[xchunk][ychunk]

            processedvalue[x][y] = processedvalue[x][y] / sectorsize

    return processedvalue



def shifty(shift, inputarray):
    xyarray = (inputarray.copy())

    return((np.roll(xyarray, shift)))



def shiftx(shift, inputarray): 
    xyarray = (inputarray.copy()).T

    return((np.roll(xyarray, shift)).T)



def skewy(slope, inputarray):
    xyarray = (inputarray.copy())

    mid = round(slope * len(xyarray) / 2)

    if slope < 0:
        mid = -mid
    
    for a in range(0, len(xyarray)):
        xyarray[a] = np.roll(xyarray[a], round(a * slope) - mid)

    return xyarray



def skewx(slope, inputarray):
    xyarray = (inputarray.copy()).T

    mid = round(slope * len(xyarray) / 2)

    if slope < 0:
        mid = -mid

    for a in range(0, len(xyarray)):
        xyarray[a] = np.roll(xyarray[a], round(a * slope) - mid)

    return xyarray.T



def rotate(degrees, inputarray):
    radians = math.radians(-degrees)
    width = len(inputarray)
    height = len(inputarray[0])

    center = [round(width / 2), round(height / 2)]

    returnarray = np.zeros(shape = (width, height), dtype = float)

    for x in range(0, width):
        for y in range(0, height):
            xcor = x - center[0]
            ycor = y - center[1]
            angle = math.atan2(ycor, xcor)
            hyp = math.sqrt(xcor ** 2 + ycor ** 2)
            dx = hyp * math.cos(angle + radians)
            dy = hyp * math.sin(angle + radians)

            if ((round(dx) + center[0]) >= 0 and (round(dx) + center[0]) < width) and ((round(dy) + center[1]) >= 0 and (round(dy) + center[1]) < height):
                returnarray[x][y] = inputarray[round(dx) + center[0]][round(dy) + center[1]]

    return returnarray



def xyarraytoarray(xyarray):
    array = []
    width = len(xyarray)
    height = len(xyarray[0])

    for a in range(0, width * height):
        array.append(xyarray[a // width][a % height])

    return array



def getborder(xyarray):
    width = len(xyarray)
    height = len(xyarray[0])

    tbx = 1
    bbx = 0

    for x in range(0, width):
        for y in range(0, height):
            if xyarray[x][y] != 0 and tbx == 1:
                tbx = 0 - x
            elif xyarray[x][y] != 0:
                bbx = width - 1 - x

    tby = 1
    bby = 0

    for y in range(0, height):
        for x in range(0, width):
            if xyarray[x][y] != 0 and tby == 1:
                tby = 0 - y
            elif xyarray[x][y] != 0:
                bby = height - 1 - y

    return [tbx, bbx, tby, bby]