def getArea(pointA, pointB):
    ax, ay = pointA
    bx, by = pointB
    return (abs(ax-bx)+1) * (abs(ay-by)+1)
                                


def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        H = len(lines)
        points = []

        for i in range(H):
            lines[i] = lines[i].replace("\n", "", 1).split(",")
            for j in range(2):
                lines[i][j] = int(lines[i][j])
            points.append((lines[i][0], lines[i][1]))
        
        maximum = 0
        for i in range(H):
            for j in range(i, H):
                area = getArea(points[i], points[j])
                if(area > maximum):
                    maximum = area

    print(maximum)
main()