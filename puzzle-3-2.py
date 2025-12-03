import math
def findNext(s, target, targetLen):
    
    pos = s.find(target)
    # print("s: ", s, " target: ", target, "targetLen: ", targetLen, "pos: ", pos)
    x = len(s) - pos
    if(x >= targetLen):
        return pos
    return -1

def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        n = 0
        for ln in lines:
            num = 0
            ln = ln.replace("\n", "", 1)
            # initial length of the number 
            targetLen = 12

            while(len(str(num)) < 12):
                # we should search for the highest digit first
                a = "987654321"
                for i, val in enumerate(a):
                    pos = findNext(ln, val, targetLen)
                    # print("returned from FindNext: ", pos)
                    # each time we get the digit for the left most position, we will reduce the targetLen by one and split the actual string from 
                    # that position to reduce search space and potential duplication error
                    if(pos > -1):
                        num = num * 10 + int(val)
                        targetLen = targetLen - 1
                        ln = ln[pos + 1: ]
                        break
            print("num: ", num)
            n = n + num
        print(n) 
main()