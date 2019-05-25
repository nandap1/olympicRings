"""
Displays the Olympic rings. 
"""
from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()
canvas.setLineWidth(8)

#Set Outline color
#Set Oval (x, y, width, height)

canvas.setOutline("blue")
canvas.drawOval(50, 10, 100, 100)

canvas.setOutline("black")
canvas.drawOval(160, 10, 100, 100)

canvas.setOutline("red")
canvas.drawOval(270, 10, 100, 100)

canvas.setOutline("yellow")
canvas.drawOval(105, 50, 100, 100)

canvas.setOutline("green")
canvas.drawOval(215, 50, 100, 100)


win.wait()

