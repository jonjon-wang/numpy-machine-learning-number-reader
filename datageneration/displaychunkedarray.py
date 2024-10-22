import turtle as t

def displaychunkedarray(screensize, chunks, pixelvalues):
    t.TurtleScreen._RUNNING = True

    sc = t.Screen()

    sc.setup(screensize, screensize)
    sc.setworldcoordinates(0, screensize, screensize, 0)

    t.hideturtle()
    t.speed("fastest")
    t.shape("square")
    t.penup()
    t.tracer(0)
    t.shapesize((screensize / chunks) / 20) # default is turtle size is 20

    for x in range(0, chunks):
        for y in range(0, chunks):
            t.goto(x * (screensize / chunks) + (screensize / chunks) / 2, y * (screensize / chunks) + (screensize / chunks) / 2)
            grayscale = pixelvalues[x * chunks + y]
            t.color((grayscale, grayscale, grayscale))
            t.stamp()

    t.update()

    t.mainloop()