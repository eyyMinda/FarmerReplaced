from Helpers import goto
from Helpers import moveToNextTile
from FarmingUtils import TillAll

def plantAll(crop, size):
	bX = size
	bY = bX
	dir = North
	
	for n in range(bX*bY):	
		if (get_entity_type() != crop):
			plant(crop)
		dir = moveToNextTile(dir)

def swapCactusNeighbours(size):
	currMeasure = measure()
	pos_x = get_pos_x()
	pos_y = get_pos_y()
	
	if (currMeasure < measure(West) and pos_x != 0):
		swap(West)
		return True
	if (currMeasure < measure(South) and pos_y != 0):
		swap(South)
		return True
	if (currMeasure > measure(East) and pos_x != size-1):
		swap(East)
		return True
	if (currMeasure > measure(North) and pos_y != size-1):
		swap(North)
		return True
	return False #if no swap occured, don't reset sort counter

def sortCactuses(size):
	bX = size
	bY = bX
	area = bX*bY
	sorted = 0
	dir = East
	
	while (sorted < area):
		sorted += 1
		if (swapCactusNeighbours(size)):
			sorted = 0
		dir = moveToNextTile(dir)
		
	
def doCactus(size):
	goto(0, 0)
	bX = size
	bY = bX
	area = bX*bY
	sorted = 0
	dir = North
	
	plantAll(Entities.Cactus, size)
	sortCactuses(size)
	harvest()