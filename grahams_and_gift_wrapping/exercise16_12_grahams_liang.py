# Convex hull Grahams
import math
import random


# Return the points that form a convex hull 
def get_convex_hull(S):   
    # Step 1
    place_p0(S)
    
    # Step 2
    sort_on_angles(S)
    S = discard_ties(S) # If two points have the same angle, discard the one that is closer to p0
    
    if len(S) < 3:
        return None
    
    # Step 3
    stack = [S[0], S[1], S[2]] # We use a s for stack
    
    # Step 4 / 5
    return remove_concave_points(S,stack)

def remove_concave_points(S,stack):
    i = 3
    while i < len(S):
        t2 = stack[len(stack) - 1]
        t1 = stack[len(stack) - 2]
      
        if which_side(t1[0], t1[1], t2[0], t2[1], S[i][0], S[i][1]) <= 0: # on the right of the line from t1 to t2
            # pop the top element off the stack
            stack.pop()
        else:
            # push a new element to the stack
            stack.append(S[i])
            i += 1

    return stack
  
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    # return math.dist((x1,y1),(x2,y2)) # alternativt   
  
# Is (x2, y2) on the right side of [x0, y0] and [x1, y1]
def which_side(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

# Place the rightmost lowest point as the first element in S 
def place_p0(S):
    """
    Places the rightmost and lowest point in the list S at index 0.

    Args:
        S (list): A list of points represented as tuples (x, y).

    Returns:
        None
    """
    rightMostIndex = 0
    rightMostX = S[0][0]
    rightMostY = S[0][1]
    
    for i in range(1, len(S)):
        if rightMostY > S[i][1]:
            rightMostY = S[i][1]
            rightMostX = S[i][0]
            rightMostIndex = i
        elif rightMostY == S[i][1] and rightMostX < S[i][0]:
            rightMostX = S[i][0]
            rightMostIndex = i     
    
    # Swap p.get(rightMostIndex) with S[0]
    if rightMostIndex != 0:
        #print(f'Bytter {S[0]} med {S[rightMostIndex]}')
        S[0], S[rightMostIndex] = S[rightMostIndex], S[0]
    

# sort_on_angles points
def sort_on_angles(S):
    for i in range(1, len(S) - 1 ):
        # Find the minimum in the S[i..len(S)-1]
        currentMin = S[i]
        currentMinIndex = i

        for j in range(i + 1, len(S)):
            if compareAngles(S[0][0], S[0][1], currentMin[0], currentMin[1], S[j][0], S[j][1]) < 0:
                currentMin = S[j]
                currentMinIndex = j

        # Swap S[i] with s[currentMinIndex] if necessary;
        if (currentMinIndex != i):
            S[currentMinIndex] = S[i]
            S[i] = currentMin

# Compare two points' angles
def compareAngles(x0, y0, x1, y1, x2, y2):
    status = which_side(x0, y0, x1, y1, x2, y2)        
    if status > 0: # Left side of the line from rightMostLowestPoint to o
        return 1
    if status <= 0.000001:
        return 0
    return -1

# If two points have the same angle, discard the one that is closer to p0
def discard_ties(S):
    """
    Discards ties from a list of points based on their distances from the first point.

    Args:
        S (list): A list of points represented as tuples (x, y).

    Returns:
        list: A new list of points with ties discarded.

    """
    d_t = [S[0]]
    
    i = 1
    while i < len(S):        
        d = distance(S[0][0], S[0][1], S[i][0], S[i][1])
        indexOfLargest = i
        k = i + 1
        while k < len(S) and compareAngles(S[0][0], S[0][1], S[i][0], S[i][1], S[k][0], S[k][1]) == 0:
            if (d < distance(S[0][0], S[0][1], S[k][0], S[k][1])):
                d = distance(S[0][0], S[0][1], S[k][0], S[k][1])
                indexOfLargest = k

            k += 1
      
        d_t.append(S[indexOfLargest])
        i = k
    
    return d_t
  