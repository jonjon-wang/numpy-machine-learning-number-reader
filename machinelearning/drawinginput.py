import turtle as t

def motion(event):
    can.unbind("<Motion>")
    x, y = event.x, event.y
    t.goto(x, y)
    if drawing == 1:
        can.bind("<Motion>", motion)

def pd(event):
    can.unbind("<ButtonPress-1>")
    t.pendown()
    if drawing == 1:
        can.bind('<ButtonPress-1>', pd)

def pu(event):
    can.unbind("<ButtonRelease-1>")
    t.penup()
    if drawing == 1:
        can.bind('<ButtonRelease-1>', pu)

def savedata(event):
    global drawing
    drawing = 0
    unbind()
    can.postscript(file = "data/temp.ps", colormode = "color")

    sc.clear()
    t.bye()

def reset(event):
    global drawing
    drawing = 0
    unbind()
    t.bye()
    drawinginput(canvassize, pensize, title)

def unbind():
    can.unbind("<Motion>")
    can.unbind("<ButtonRelease-1>")
    can.unbind("<ButtonPress-1>")
    can.unbind("<space>")
    can.unbind("<ButtonPress-3>")



def drawinginput(cs, ps, tt):
    t.TurtleScreen._RUNNING=True

    global canvassize
    canvassize = cs

    global pensize
    pensize = ps

    global title
    title = tt

    global drawing
    drawing = 1

    global sc
    sc = t.Screen()

    global can
    can = t.getcanvas()

    sc.clear()
    sc.title(title)
    sc.setup(canvassize, canvassize)
    sc.setworldcoordinates(0, canvassize, canvassize, 0)

    t.speed("fastest")
    t.delay(0)
    t.pensize(pensize)
    t.hideturtle()
    t.penup()

    sc.listen()
    can.bind('<Motion>', motion)
    can.bind('<ButtonPress-1>', pd)
    can.bind('<ButtonRelease-1>', pu)
    can.bind("<ButtonPress-3>", reset)
    can.bind("<space>", savedata)

    t.mainloop()