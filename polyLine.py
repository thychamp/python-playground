
# bbox dimensions
minX = -109 
minY = 37
maxX = -102
maxY = 40

def point_in_box(x, y):
    # in or out
    if x>minX and x<maxX and y>minY and y<maxY:
        return True
    elif x < minX or x > maxX or y < minY or y > maxY:
        return False
    else:
        return True

numPointInBbox = 0
polyline = [(-105, 38), (-102, 39), (-104, 37), (-103, 40)]
for point in polyline: 
    x = point[0]
    y = point[1]
    result = point_in_box(x, y) 
    if result == True:
        numPointInBbox = numPointInBbox + 1

if numPointInBbox == len(polyline):
    print("Polyline inside bbox")
else:
    print("Polyline outside bbox")