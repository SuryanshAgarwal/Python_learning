import math
def check_circle(c1,r1,c2,r2):
    d = math.sqrt(sum((a-b)**2 for a,b in zip(c1,c2)))
    if d<r1:
        print('Circle 2 is inside Circle 1')
    if d<r2:
        print('Circle ')
    if d>r1 and d>r2:
