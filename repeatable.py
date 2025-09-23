# TODO: add remade checkSeeds function by checking the cost of current selected entity
# and if there is enough of it for at least a whole field. Otherwise run replant to farm more

def runLoop(times, info):
    for i in range(times):
        quick_print("Loop for", info[1], [i, times])
        replant(info[0], info[1], 0.8, True)