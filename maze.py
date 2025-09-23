import FarmingUtils
import FarmingChecks
from Replant import replant
from Helpers import fieldGrid
from Helpers import goto

def startMaze():
    clear()
    plant(Entities.Bush)
    while not FarmingChecks.is_over(Entities.Hedge) and not FarmingChecks.is_over(Entities.Treasure):
        useSubstance()
    solveMaze()
    
def useSubstance():
	n_substance = get_world_size() * 1 #num_unlocked(Unlocks.Mazes)
	if num_items(Items.Weird_Substance) >= n_substance:
		use_item(Items.Weird_Substance, n_substance)
	else:
		replant(get_world_size(), Entities.Bush, 0.3, False)

def solveMaze():

    facing = 0
    directions = [North, East, South, West]

    while get_entity_type() != Entities.Treasure:
        x = get_pos_x()
        y = get_pos_y()

        move(directions[facing % 4])

        facing += 1
        if x == get_pos_x() and y == get_pos_y():
            facing += 2

    harvest()


def findTreasure():
    been = []
    path = [[get_pos_x(), get_pos_y()]]

    while True:
        if FarmingChecks.is_over(Entities.Treasure):
            harvest()
            break

        posX = get_pos_x()
        posY = get_pos_y()
        pos = [posX, posY]
        freedom = getBranching()
        moved = False

        for direction in freedom:
            dirpos = direction[1]
            pathContains = False
            beenContains = False

            for p in path:
                if (p[0] == dirpos[0]) and (p[1] == dirpos[1]):
                    pathContains = True
            for p in been:
                if (p[0] == dirpos[0]) and (p[1] == dirpos[1]):
                    beenContains = True

            if (beenContains == False) and (pathContains == False):
                move(direction[0])
                path.append(pos)
                moved = True
                break
        if moved == False:
            a = path.pop()
            if len(freedom) == 2:
                been.pop()
            been.append(pos)
            FarmingUtils.backtrack(a, posX, posY)


def getBranching():
    directions = [North, East, South, West]
    branching = []
    ind = 0
    for direction in directions:
        initX = get_pos_x()
        initY = get_pos_y()
        move(direction)
        newX = get_pos_x()
        newY = get_pos_y()
        wall = initX == newX and initY == newY
        if not wall:
            backInd = ind
            if ind >= 2:
                backInd -= 2
            else:
                backInd += 2
            move(directions[backInd])
            branching.append([direction, [newX, newY]])
        ind += 1
    return branching