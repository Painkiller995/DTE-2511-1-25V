# Convex hull Gift Wrapping
import math
import random


# Return the points that form a convex hull 
def get_convex_hull(myPoints):   
    # Step 1
    h0 = get_rightmost_lowest_point(myPoints)
    
    H = [h0]    
    t0 = h0
        
    # Step 2 and Step 3
    while True:   
        t1 = myPoints[0]
        for i in range(1, len(myPoints)):
            status = which_side(t0[0], t0[1], t1[0], t1[1], myPoints[i][0], myPoints[i][1])
        
            if status < 0:  # Right side of the line
                t1 = myPoints[i]
            elif status == 0:
                if distance(myPoints[i][0], myPoints[i][1], t0[0], t0[1]) > distance(t1[0], t1[1], t0[0], t0[1]):
                    t1 = myPoints[i]
      
        if t1[0] == h0[0] and t1[1] == h0[1]: 
            break; # A convex hull is found
        else:
            H.append(t1)
            t0 = t1
    
    return H
  
# Return the rightmost lowest point in S 
def get_rightmost_lowest_point(p):
    rightMostIndex = 0
    rightMostX = p[0][0]
    rightMostY = p[0][1]
    
    for i in range(1, len(p)):
        if rightMostY > p[i][1]:
            rightMostY = p[i][1]
            rightMostX = p[i][0]
            rightMostIndex = i
        elif rightMostY == p[i][1] and rightMostX < p[i][0]:
            rightMostX = p[i][0]
            rightMostIndex = i   
    
    return p[rightMostIndex]
  
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
  
# Is (x2, y2) on the right side of [x0, y0] and [x1, y1]  
def which_side(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
  
#coordinates = input("Enter the points in one line separated by space: ")
#c = coordinates.split()
#print(c)
#points = [[float(c[i]), float(c[i + 1])] for i in range(0, len(c) - 2, 2)]
#print(points)
points = []
for i in range(50):
    x, y = random.random() *100, random.random() * 100
    points.append([x,y])

# Nine points that forms a convex hull p0 to p8
# Two of the points, p2[4,2], p4[4,3], and p6[2,4] are not part of the
# Convex hull 

points2 = [[5.0,2.0],[1.0,1.0],[4.0,2.0],[6.0,4.0],
          [4.0,3.0],[5.0,6.0],[2.0,4.0],[3.0,6.0],[1.0,3.0]]

convexHull = get_convex_hull(points)   
print("The convex hull for points is ")
print(convexHull)
convexHull = get_convex_hull(points2)   
print("\nThe convex hull for points2 is ")
print(convexHull)
