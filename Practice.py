import math
import pandas as pd
import numpy as np
import csv

gridSize= 512
centre=[gridSize/2.0,gridSize/2.0]
centre1=[0.0,gridSize/2.0]
centre2=[gridSize,gridSize]
Radius = 35

lineStart1 = [150,150]
lineEnd1 = [360,150]
lineStart2 = [360,150]
lineEnd2 = [360,360]
lineStart3 = [360,360]
lineEnd3 = [150,360]

grid = np.zeros(shape=(gridSize,gridSize,4))
 
# distance field for circle
def distanceCircle(centre, radius,point):
    distance = math.sqrt((centre[0]-point[0])**2 + (centre[1]-point[1])**2)
    return distance-radius

def dotproduct(v1, v2):
        s = 0
        for a,b in zip(v1, v2):
                s += a*b
        return s

def length(v):
        return math.sqrt(dotproduct(v, v))

def lengthBtwPoints(v1, v2):
        return math.sqrt((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)

# distance field for Line
def distanceLine(lineStart, lineEnd, point):
        v1 = np.subtract(lineEnd, lineStart)
        v2 = np.subtract(lineStart, lineEnd)
        p1 = np.subtract(point, lineStart)
        p2 = np.subtract(point, lineEnd)
        theta1 = math.acos(dotproduct(v1, p1)/(length(v1) * length(p1)))
        theta1 = theta1*(180/math.pi)
        theta2 = math.acos(dotproduct(v2, p2)/(length(v2) * length(p2)))
        theta2 = theta2*(180/math.pi)
        if theta1 >= 90 and theta2 < 90:
                l = lengthBtwPoints(lineStart, point)
        elif theta1 < 90 and theta2 >= 90:
                l = lengthBtwPoints(lineEnd, point)
        else:
                numerator = abs(((lineEnd[1]-lineStart[1])*point[0])-((lineEnd[0]-lineStart[0])*point[1])+(lineEnd[0]*lineStart[1])-(lineEnd[1]*lineStart[0]))
                denom = lengthBtwPoints(lineEnd,lineStart)
                l = numerator/denom
        return l
fmax=-10
fmin=10

# fill up the distance field 
x = []
y = []
distance = []
for i in range(gridSize):
    for  j in range(gridSize):
        # grid.append([i,j,0,min(distanceCircle(centre1, 25, [i,j]),distanceCircle(centre2, 20, [i,j]))])
        grid[i][j][0]=i
        x.append(i)
        grid[i][j][1]=j
        y.append(j)
        grid[i][j][2]=0
        grid[i][j][3]=distanceLine(lineStart1,lineEnd1,[i,j])
        grid[i][j][3]= min(grid[i][j][3], distanceLine(lineStart2, lineEnd2, [i,j]))
        grid[i][j][3]= min(grid[i][j][3], distanceLine(lineStart3, lineEnd3, [i,j]))
        # grid[i][j][3]=distanceCircle(centre, Radius, [i,j])
        # grid[i][j][3]=min(grid[i][j][3],distanceCircle(centre1, 25, [i,j]))
        # grid[i][j][3]=min(grid[i][j][3],distanceCircle(centre2, 20, [i,j]))
        distance.append(grid[i][j][3])
        fmin=min(fmin,grid[i][j][3])
        fmax=max(fmax,grid[i][j][3])

fdelta=fmax-fmin
#write a image 
from PIL import Image
from matplotlib import cm
cmap = cm.get_cmap('seismic',lut=256)

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)

for i in range(gridSize):
    for  j in range(gridSize):
        val=(grid[i][j][3]-fmin)/fdelta
        rgba = cmap(val)
        data[gridSize-1-j][i]=[int(rgba[0]*255),int(rgba[1]*255),int(rgba[2]*255)]
        #data[gridSize-1-j][i]=[((grid[i][j][3]-fmin)/fdelta)*255,(1-(grid[i][j][3]-fmin)/fdelta)*255,255]

import matplotlib.pyplot as plt
plt.contourf(x,y,distance)
imgplot = plt.imshow(data)
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()



# #write the distane field 
f = open("line_c.txt","w")
f.write("x,y,z,val \n")

for i in range(gridSize):
    for  j in range(gridSize):
        f.write(str(grid[i][j][0])+","+str(grid[i][j][1])+","+str(grid[i][j][2])+",")
        # if grid[i][j][3]< 0 :
        #     f.write("-50")    
        # else :
        
        f.write(str(grid[i][j][3]))
        f.write("\n")