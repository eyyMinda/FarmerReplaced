from Helpers import moveToNextTile

def use_water(water = 0.3):
	tileWatered = get_water() <= water
	haveWater = num_items(Items.Water) > 0
	if tileWatered and haveWater:
		use_item(Items.Water)
		
def use_fertilizer():
	if num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
		
def Till():
	if get_ground_type() == Grounds.Grassland:
		till()
		
def TillAll():
	bX = get_world_size()
	bY = bX
	dir = North
	
	for n in range(bX*bY):
		till()
		dir = moveToNextTile(dir)