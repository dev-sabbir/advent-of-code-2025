# BFS will not work because of the search space

def makeState(str, numOfLight):
    ret = []
    if(str[0] == '{'): # expected indicator description
        str = str.replace("{", "", 1)
        str = str.replace("}", "", 1)
        str = str.split(",")

        for x in str:
            x = int(x)
                
            ret.append(x) 
            
    elif(str[0] == '('): # button wiring semantics
        str = str.replace("(", "", 1)
        str = str.replace(")", "", 1)
        str = str.split(",")
        #creating a string of all 0s
        for i in range(numOfLight):
            ret.append(0)
        if(len(str[0]) > 0):
            for x in str:
                x = int(x)
                ret[x] = 1
    return ret

def calculateNextState(a, b):
    ret = []

    for i in range(len(a)):
        ret.append(a[i] + b[i])
    return tuple(ret)

def isValid(a, b):
    for i in range(len(a)):
        if( b[i] > a[i]):
            return False
    return True

def solve(line):
    numberOfLights = len(line[0]) - 2
    # print(line)
    finalState = tuple(makeState(line[len(line) - 1], numberOfLights))
    initialStates = []

    buttons = []

    for i in range(1, len(line) -1):
        buttons.append(line[i])

    buttons.sort(key=len)
    buttons.reverse()

    for i in range(len(buttons)):
        initialStates.append(tuple(makeState(buttons[i], numberOfLights)))

    initState = tuple(makeState("()", numberOfLights))

    print(finalState)
    print(initialStates)

    states = [initState]
    step =0
    found = False
    visited = {}
    while(step < 1000 and not found):
        print("states length after step ", step, ' is ', len(states))
        tempStates = []
        while(len(states)):
            item = states.pop(0)
            visited[item] = 1
            for nxtItem in initialStates:
                nextState = calculateNextState(list(item), list(nxtItem))
                if(nextState == finalState):
                    found = True
                else:
                    if(nextState not in visited and isValid(list(finalState), list(nextState))):
                        tempStates.append(nextState)
        
        step = step + 1
        states = []
        states = list(set(tempStates))
    
    return step if found else 0

def main():
    total = 0
    filepath = "a.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            line = line.replace("\n", "", 1).split(" ")
            #print("started processing line ", i)
            stepsNeeded = solve(line)
            #print(":steps needed for line ", i, "is ", stepsNeeded)
            total = total + stepsNeeded
            i += 1
        print(total)
main()