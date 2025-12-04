def findNeighbours(i, j, X, Y):
    indexes = []
    dirX = [0, 1, -1, 0, 1, -1, -1, 1]
    dirY = [1, 0, 0, -1, 1, 1, -1, -1]
    for d in range(8):
        newX = i + dirX[d]
        newY = j + dirY[d]
        if(newX >= 0 and newY >= 0 and newX < X and newY < Y):
            indexes.append((newX, newY))
    return indexes
def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        x = len(lines)
        y = len(lines[0]) - 1
        
        n = 0
        target = 4
        for i in range(x):
            for j in range(y):
                indexes = findNeighbours(i, j, x, y)
                
                total = 0
                for (xx, yy) in indexes:
                    if(lines[xx][yy] == '@'):
                        total = total + 1
                if(total < target and lines [i][j] == '@'):
                    n = n + 1
    print(n)
            
main()

