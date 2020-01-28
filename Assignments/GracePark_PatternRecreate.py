from random import random

w = 900
h = 900
size (w, h)
squareSize = 100
squareCount = 4

a = int((w/squareSize)*2)
b = int((h/squareSize)*2)

def makeSquares(uhh, idk): 
    for c in range(squareCount):
        rect(uhh, idk, squareSize*((c+1)/squareCount), squareSize*((c+1)/squareCount))

rotate(315, center=(w/10,h))
fill(None)
strokeWidth(10)
for y in range(b):
    for x in range(a):
        stroke((200/(x+1))/255, 20*x/255, 180/255, 1)
        makeSquares(x*squareSize, y*squareSize)
        

# if (random() <= 0.4):
#     stroke(80/255, 252/255, 1, 1)
# else: