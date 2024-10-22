import turtle as t

screensize = [800, 600]

bordersize = [50, 50]

nodesize = [1, 1, 3]
linesize = 2

usablescreen = [screensize[0] - (2 * bordersize[0]), screensize[1] - (2 * bordersize[1])]

def displaydata(dataset): #does not work

    [n2, b2, w3, dn2, db2, dw3] = dataset

    sc = t.Screen()
    
    sc.clear()
    sc.setup(screensize[0], screensize[1])
    sc.setworldcoordinates(-bordersize[0], -bordersize[1], screensize[0] - bordersize[0], screensize[1] - bordersize[1])

    t.penup()
    t.pensize(linesize)
    t.hideturtle()
    t.tracer(0)
    t.speed("fastest")
    t.colormode(1.0)
    t.shape("circle")
    t.shapesize(nodesize[0], nodesize[1], nodesize[2])

    maxweight = 0
    for a in range(0, len(w3)):
        for b in range(0, len(w3[a])):
            for c in range(0, len(w3[a][b])):
                maxweight = max([max(w3[a][b]), abs(min(w3[a][b])), maxweight])

    maxbias = 0
    for a in range(1, len(b2)):
        for b in range(0, len(b2[a][0])):
            maxbias = max([max(b2[a][0]), abs(min(b2[a][0])), maxbias])

    n2location = [] #try to center each set of nodes also axis are backwards probably
    for a in range(0, len(n2)):
        n1location = []
        for b in range(0, len(n2[a][0])):
            n1location.append([(a / (len(n2) - 1) * usablescreen[0]), (b / len(n2[a][0]) * usablescreen[1]) + 0.5 * (1 / len(n2[a][0]) * usablescreen[1])])
        n2location.append(n1location)

    for a in range(1, len(w3)):  #make stamp and weights seperate stages so they do not overlap
        for b in range(0, len(w3[a])):
            for c in range(0, len(w3[a][b])):
                t.setpos(n2location[a - 1][c][0], n2location[a - 1][c][1])

                displayvalue = 0.5 - min(1, max(-1, w3[a][b][c] / maxweight)) / 2
                t.pencolor((displayvalue, 0.5, 0.5))
                t.pendown()

                t.setpos(n2location[a][b][0], n2location[a][b][1])
                t.penup()

    for a in range(0, len(n2)):  #make stamp and weights seperate stages so they do not overlap
        for b in range(0, len(n2[a][0])):
            t.setpos(n2location[a][b][0], n2location[a][b][1])
            displayvalue = 1 - n2[a][0][b]
            t.fillcolor((displayvalue, displayvalue, displayvalue))

            if a == 0:
                t.pencolor((0.5, 0.5, 0.5))
            else:
                displayvalue = 0.5 - min(1, max(-1, b2[a][0][b] / maxbias)) / 2
                t.pencolor((displayvalue, 0.5, 0.5))

            t.stamp()


    t.update()
    t.mainloop()




    