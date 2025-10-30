from Helpers import fieldGrid
from FarmingUtils import Till
from FarmingUtils import use_water

def polyculture(size, water, buySeeds):
    field = fieldGrid(size, Entities.Grass)
    while True:
        for x in range(size):
            for y in range(size):
				companion = get_companion()
				entity = field[x][y]
				if can_harvest():
					harvest()
					if entity == Entities.Carrot:
						Till()
						#checkSeeds(size, entity, buySeeds)
					plant(entity)
					use_water()
					if companion != None:
						field[companion[1][0]][companion[1][1]] = companion[0]
				else:
					plant(Entities.Grass)
				move(North)
			move(East)
