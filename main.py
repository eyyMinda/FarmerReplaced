from Maze import startMaze
from Poly import polyculture
from Replant import replant
from Replant import replantPumpkin
from Cactus import doCactus
from FarmingUtils import TillAll


def start():
    clear()
    do_a_flip()

    treasure = False

    poly = True

    size = get_world_size()
    entity = Entities.Cactus or "mix" #
    water = 0.3
    buySeeds = size * size

	if entity == Entities.Cactus and treasure == False and poly == False:
		TillAll()
    while True:
        if treasure == True:
            startMaze()
        elif poly == True:
            polyculture(size, water, 1)
        else:
            if entity == Entities.Cactus:
                doCactus(size)
            elif entity == Entities.Pumpkin:
                replantPumpkin(size, entity, buySeeds)
            else:
                replant(size, entity, water, buySeeds)
                
start()