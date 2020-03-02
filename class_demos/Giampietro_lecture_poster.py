from chiplotle import *
import math
import random

lecture = """Rob Giampietro
March 2
5:30pm Reception
6pm    Talk
Steinberg Auditorium"""

plotter = instantiate_plotters( )[0]
plotter.rotate(angle=90)
plotter.set_origin_bottom_left()

width = plotter.margins.soft.width
height = plotter.margins.soft.height


# Talk title
plotter.select_pen(3)

charwidth = int(width/61)
charheight = int((height/3)/9)
labelbox = (int(width/2), int((height/3)*2), int(width/2), charheight*6)

title = shapes.group([])

for i, line in enumerate(lecture.split("\n")):
    l = shapes.label(line, charwidth/400.0, charheight/400.0)
    transforms.offset(l, (labelbox[0], int(labelbox[1]-(i*charheight*1.1))))
    title.append(l)
    
plotter.write(title)


# Calculate the box around the talk title. Ugly.
labelbox = (int(labelbox[0]-(width/70)),
            int(labelbox[1]+charheight*1.2),
            width-int(labelbox[0]-(width/70)),
            labelbox[3]
            )

# get the distance we should use for the arc above the title box
if labelbox[2] < height-labelbox[1]:
    m = labelbox[2]
else:
    m = height-labelbox[1]

def drawArc(limit, center, arc, group):
    for r in range(limit[0], limit[1], random.randrange(100,200,limit[2])):
        a = shapes.arc_circle(r, arc[0], arc[1])
        transforms.offset(a, center)
        group.append(a)


plotter.select_pen(1)

pass_one = [
            [(100, m, 5), (labelbox[0]+labelbox[2], labelbox[1]), (math.pi/2, math.pi)],
            [(100, labelbox[3], 5), (labelbox[0], labelbox[1]-labelbox[3]), (math.pi/2, math.pi*2)],
            [(100, labelbox[3], 5), (labelbox[0], labelbox[1]), (0, math.pi*1.5)],
            [(100, width-1000, 5), (0, 0), (0, math.pi/2)],
            [(100, height-labelbox[1], 5), (width, height), (math.pi, math.pi*1.5)],
            [(100, labelbox[2], 5), (labelbox[0]+labelbox[2], labelbox[1]-labelbox[3]), (math.pi, math.pi*1.5)],
           ]

g = shapes.group([])
for limit, center, arc in pass_one:
     drawArc(limit, center, arc, g)
plotter.write(g)

plotter.select_pen(2)

pass_two = [
            [(100, m, 27), (labelbox[0]+labelbox[2], labelbox[1]), (math.pi/2, math.pi)],
            [(100, labelbox[3], 27), (labelbox[0], labelbox[1]-labelbox[3]), (math.pi/2, math.pi*2)],
            [(100, labelbox[3], 27), (labelbox[0], labelbox[1]), (0, math.pi*1.5)],
            [(100, width-1000, 27), (0, 0), (0, math.pi/2)],
            [(100, height-labelbox[1], 27), (width, height), (math.pi, math.pi*1.5)],
            [(100, labelbox[2], 27), (labelbox[0]+labelbox[2], labelbox[1]-labelbox[3]), (math.pi, math.pi*1.5)],
           ]

g = shapes.group([])
for limit, center, arc in pass_one:
     drawArc(limit, center, arc, g)
plotter.write(g)

plotter.select_pen(0)

