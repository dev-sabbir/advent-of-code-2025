import math

def dist(a, b):
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2) + pow((a[2] - b[2]), 2))


def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        H = len(lines)
        parent = {}
        circuitSize = {} 
        distanceList = [] # ordered list of distance
        distanceToItemMap = {} 
        target = 1000 # the number or connection to be made


        for i in range(H):
            lines[i] = lines[i].replace("\n", "", 1).split(",")
            for j in range(3):
                lines[i][j] = int(lines[i][j])
            lines[i] = (lines[i][0], lines[i][1], lines[i][2])
            parent[lines[i]] = lines[i]
            circuitSize[lines[i]] = 1
        
        for i in range(H):
            for j in range(H):
                if(j < i):
                    distance = dist(lines[i], lines[j])
                    distanceList.append(distance)
                    distanceToItemMap[distance] = (lines[i], lines[j])
        
        # sorting the distances
        distanceList.sort()
        

        def findParent(a):
            if(parent[a] == a):
                return a
            parent[a] = findParent(parent[a])
            return parent[a]
        
        def updateParent(a, b):
            for i in parent:
                if(parent[i] == a):                    
                    parent[i] = findParent(b)
                    circuitSize[i] = 0
        
        def union(a, b):
            a = findParent(a)
            b = findParent(b)
            
            if(a != b):
                if(circuitSize[a] >= circuitSize[b]):
                    parent[b] = a
                    updateParent(b, a)
                    circuitSize[a] = circuitSize[a] + circuitSize[b]
                    circuitSize[b] = 0
                else:
                    parent[a] = b
                    updateParent(a, b)
                    circuitSize[b] = circuitSize[a] + circuitSize[b]
                    circuitSize[a] = 0

        
        for i in range(target):
            (a, b) = distanceToItemMap[distanceList[i]]
            union(a, b)
        
        # sorting the dictionary by circuitSize
        circuitSize = sorted(circuitSize.items(), key=lambda item: item[1], reverse=True)
        distanceToItemMap = sorted(distanceToItemMap.items(), key=lambda item: item[0])
        
        
        total = 1
        for i in range(3):
            _, value = circuitSize[i]
            total = total * value
        print(total)

main()