w=1000
h=1000
size(w,h)

blendMode("multiply")
path = BezierPath()
# move to a point
path.moveTo((0, 0))
# line to a point
path.lineTo((1000, 100))
path.lineTo((300, 250))
# close the path
path.closePath()

for i in range(50):
    fill(0,0,0,0)
    rotate(50)    
    stroke(1, random(), random(), 0.1)
    strokeWidth(120)
    drawPath(path)
    translate(10, 50)

path = BezierPath()
# move to a point
path.moveTo((0, 0))
# line to a point
path.lineTo((1000, 100))
path.lineTo((300, 250))
# close the path
path.closePath()

for i in range(50):
    fill(0,0,0,0)
    rotate(50)    
    stroke(1, random(), random(), 0.1)
    strokeWidth(120)
    drawPath(path)
    translate(10, 50)
    
# newPage(1000, 1000)
# padding=5

# width = range(0, width())
# height = range(0, height())

# def draw(x, y, width, height):
#     path = BezierPath()
#     # move to a point
#     path.moveTo((0, 0))
#     # line to a point
#     path.lineTo((1000, 100))
#     path.lineTo((300, 250))
#     # close the path
#     path.closePath()
#     for i, x in enumerate(width):
#         for y in height: 
#             draw(x,y,width,height) 
        
# def pattern():
#     for i, x in enumerate(width):
#         for y in height:
#             if i % 2 == 0:
#                 y = y+(module/2)    
#             image = module - padding
#             d = padding/2
#             draw(x,y,image,image)
         



             
    
    