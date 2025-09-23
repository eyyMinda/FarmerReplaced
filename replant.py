import FarmingUtils
import FarmingChecks
from Helpers import fieldGrid
from Helpers import goto

plantData = {
	Entities.Grass: { "till": False },
	Entities.Bush: { "till": False },
	Entities.Tree: { "till": False },
	Entities.Carrot: { "till": True },
	Entities.Cactus: { "till": True },
	Entities.Sunflower: { "till": True },
	"mix": { "till": False }
}

#---------- General
def replant(size, entity, water, buySeeds):
    for x in range(size):
        for y in range(size):

            if can_harvest():
                harvest()
                if plantData[entity]["till"]:
                    FarmingUtils.Till()
                    #if buySeeds > 0 and x == 0 and y == 0:
                        #checkSeeds(size, entity, buySeeds)

                if entity == Entities.Bush or entity == "mix":
                    if x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0:
                        plant(Entities.Tree)
                        FarmingUtils.use_fertilizer()
                    elif entity == "mix":
                        FarmingUtils.Till()
                        plant(Entities.Carrot)

                if entity != Entities.Grass and entity != "mix":
                    plant(entity)

                    FarmingUtils.use_water()
            # y end
            move(North)
        # x end
        move(East)


#-------- Pumpkins
def replantPumpkin(size, entity, buySeeds):
    field = fieldGrid(size, False)

    for z in range(3):
        for x in range(size):
            for y in range(size):

                if not FarmingChecks.is_over(entity):
                    FarmingUtils.Till()
                    #if buySeeds > 0 and z == 0 and x == 0 and y == 0:
                        #checkSeeds(size, entity, buySeeds)
                    plant(entity)

                    if z > 0:
                        field[x][y] = True
                else:
                    if z > 0 and can_harvest():
                        field[x][y] = False

                move(North)
            # y end
            move(East)
        # x end
    # z end
    fillRemaining(size, entity, field)

    harvest()
    goto(0, 0)


def fillRemaining(size, entity, field):
    keepChecking = True
    while keepChecking:
        hasLeft = False
        for x in range(size):
            for y in range(size):
                if field[x][y] == True:
                    hasLeft = True
                    goto(x, y)
                    if not FarmingChecks.is_over(entity):
                        FarmingUtils.Till()
                        plant(entity)
                    elif can_harvest():
                        field[x][y] = False

        keepChecking = hasLeft