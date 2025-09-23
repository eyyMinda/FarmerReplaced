# Utils
def is_even(x):
	return x % 2 == 0
def is_odd(x):
	return x % 2 == 1
	
def goto(x, y):
    yDist = get_pos_y() - y  # Positive if drone is north of the target space
    xDist = get_pos_x() - x  # Positive if drone is east of the target space
    halfWorldSize = get_world_size()/2
    while get_pos_y() != y:
        if yDist >= halfWorldSize or (-halfWorldSize <= yDist and yDist < 0):
            move(North)
        else:
            move(South)
    while get_pos_x() != x:
        if xDist >= halfWorldSize or (-halfWorldSize <= xDist and xDist < 0):
            move(East)
        else:
            move(West)
            
def backtrack(route, x, y):
    if x > route[0]:
        move(West)
    elif x < route[0]:
        move(East)
    elif y > route[1]:
        move(South)
    elif y < route[1]:
        move(North)


def fieldGrid(size, element):
    xArr = []
    for x in range(size):
        yArr = []
        for y in range(size):
            yArr.append(element)
        xArr.append(yArr)
    return xArr


    
def moveToNextTile(dir):
	bX = get_world_size() #Farm width (x Boundary)
	bY = bX #Farm height (y Boundary)
	cX = get_pos_x() #Current X position
	cY = get_pos_y() #Current Y position
	if (dir==East):
		if (cX+1==bX):
			dir=North
	elif (dir==West):
		if (cX==0):
			dir=North
	elif (dir==North):
		if (cX+1==bX):
			dir=West
		elif (cX==0):
			dir=East
			
	move(dir)
	return dir