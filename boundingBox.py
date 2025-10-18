# bbox dimensions
minX = -109 
minY = 37
maxX = -102
maxY = 40

# user input
x = int(input("Input X coordinate: "))
y = int(input("Input Y coordinate: "))

# in or out
if x>minX and x<maxX and y>minY and y<maxY:
    print("Your coordinate is inside the bbox")
elif x < minX or x > maxX or y < minY or y > maxY:
    print("Your coordinate is not inside the bbox")
else:
    # corners
    if x == minX and y == minY:
        print("Point is on the Bottom-Left corner.")
    elif x == maxX and y == minY:
        print("Point is on the Bottom-Right corner.")
    elif x == maxX and y == maxY:
        print("Point is on the Top-Right corner.")
    elif x == minX and y == maxY:
        print("Point is on the Top-Left corner.")
    # edges
    elif x == minX:
        print("Point is on the Left edge.")
    elif x == maxX:
        print("Point is on the Right edge.")
    elif y == minY:
        print("Point is on the Bottom edge.")
    elif y == maxY:
        print("Point is on the Top edge.")









# --- Algorithm to check the spatial relationship ---

# 1. Check if the point is strictly INSIDE the box
if minX < x < maxX and minY < y < maxY:
    print(f"Point ({x}, {y}) lies inside the bbox.")

# 2. Check if the point is strictly OUTSIDE the box
elif x < minX or x > maxX or y < minY or y > maxY:
    print(f"Point ({x}, {y}) lies outside the bbox.")

# 3. Otherwise, the point must be ON THE BOUNDARY
else:
    # Check for corners first
    if x == minX and y == minY:
        print("Point is on the Bottom-Left corner.")
    elif x == maxX and y == minY:
        print("Point is on the Bottom-Right corner.")
    elif x == maxX and y == maxY:
        print("Point is on the Top-Right corner.")
    elif x == minX and y == maxY:
        print("Point is on the Top-Left corner.")
    # Check for edges
    elif x == minX:
        print("Point is on the Left edge.")
    elif x == maxX:
        print("Point is on the Right edge.")
    elif y == minY:
        print("Point is on the Bottom edge.")
    elif y == maxY:
        print("Point is on the Top edge.")

