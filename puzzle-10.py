def makeBinaryString(str, numOfLight):
    # print(str)
    ret = ""
    if(str[0] == '['): # expected indicator description
        for i in range(1, len(str) - 1):
            if(str[i] == '.'):
                ret = ret + "0"
            elif(str[i] == '#'):
                ret = ret + "1"
    elif(str[0] == '('): # button wiring semantics
        str = str.replace("(", "", 1)
        str = str.replace(")", "", 1)
        str = str.split(",")
        #creating a string of all 0s
        for i in range(numOfLight):
            ret = ret + "0"
        if(len(str[0]) > 0):
            ret = list(ret)
            for x in str:
                x = int(x)
                
                ret[x] = "1"
            ret = "".join(ret)
    return ret

def calculateNextState(str1, str2):
    ret = ""

    for i in range(len(str1)):
        if((str1[i] == '1' and str2[i] == '1') or (str1[i] == '0' and str2[i] == '0')):
            ret = ret + "0"
        else:
            ret = ret + "1"
    return ret

def solve(line):
    numberOfLights = len(line[0]) - 2

    finalState = makeBinaryString(line[0], numberOfLights)
    initialStates = []
    for i in range(1, len(line) -1):
        initialStates.append(makeBinaryString(line[i], numberOfLights))

    initState = makeBinaryString("()", numberOfLights)

    # print(finalState)
    # print(initialStates)

    states = [initState]
    step =0
    found = False
    visited = {}
    while(step < 1000 and not found):
        # print("states after step ", step, " are ", states)
        tempStates = []
        while(len(states)):
            item = states.pop(0)
            visited[item] = 1
            for nxtItem in initialStates:
                nextState = calculateNextState(item, nxtItem)
                if(nextState == finalState):
                    found = True
                else:
                    if(nextState not in visited):
                        tempStates.append(nextState)
        
        step = step + 1
        states = []
        states = list(set(tempStates))
    
    return step if found else 0

def main():
    total = 0
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            line = line.replace("\n", "", 1).split(" ")
            print("started processing line ", i)
            stepsNeeded = solve(line)
            print(":steps needed for line ", i, "is ", stepsNeeded)
            total = total + stepsNeeded
            i += 1
        print(total)
main()