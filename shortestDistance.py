data = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]

#simple distance formula
def euclideanDistance(point1, point2):
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2) ** 0.5

#shortest distance algorithm
#double loops, use range with len
#conditional check for minDistance
#update the new minDistance with the distance
#preserve the points that return that distance
def returnShortestDistance(points):
    minDistance = 99999
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            dist = euclideanDistance(points[i],points[j])
            if dist < minDistance:
                minDistance = dist
                point1 = points[i]
                point2 = points[j]
    return [point1, point2]

print(returnShortestDistance(data))