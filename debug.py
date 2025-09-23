from Maze import startMaze
from Poly import polyculture
from Replant import replant
from Replant import replantPumpkin

def start():
    clear()
    do_a_flip()

    size = get_world_size()
    entity = Entities.Pumpkin
    water = 0.3
    buySeeds = size * size

    # Retrieve Stats
    debug = False

    loops = 5
    function = 2
    list = [size, entity, buySeeds]

    treasure = False
    poly = True

    while True:
        if debug == False:
            if treasure == True:
                startMaze()
            elif poly == True:
                polyculture(size, water, 1)
            else:
                if entity == Entities.Pumpkin:
                    replantPumpkin(size, entity, buySeeds)
                else:
                    replant(size, entity, water, buySeeds)
        else:
            if entity == Entities.Pumpkin:
                function = 1
            stats = statsLoop(loops, function, list)

            while True:
                print(stats)

                findSpecific = None

                if findSpecific != None:
                    for i in range(len(stats[1])):
                        if stats[1][i][0] == findSpecific:
                            print(stats[1][i])
                do_a_flip()


def statsLoop(loops, function, list):
    # functions
    # [0] - replant
    # [1] - replantPumpkin
    # [2] - polyculture
    # [3] - startMaze

    # list
    # [0] - size
    # [1] - entity
    # [2] - buySeeds

    startInventory = get_inventory()
    invLen = len(startInventory)

    profit = []
    startTime = get_time()

    if function == 2:
        polyculture(loops, list[0], 0.3, 1)
    for z in range(loops):
        if function == 0:
            replant(list[0], list[1], 0.3, list[2])
        elif function == 1:
            replantPumpkin(list[0], list[1], list[2])
        elif function == 3:
            startMaze()

    endTime = get_time()
    endInventory = get_inventory()

    ignoreItems = [Items.Water]

    for i in range(invLen):
        currItem = startInventory[i][0]
        startAmount = startInventory[i][1]
        endAmount = endInventory[i][1]
        moveOn = True
        for n in range(len(ignoreItems)):
            if ignoreItems[n] == currItem:
                moveOn = False

        if moveOn == True and endAmount != startAmount:
            profitAmount = endAmount - startAmount
            profit.append([currItem, profitAmount])

    timeSpent = endTime - startTime
    return [timeSpent, profit]
    
start()