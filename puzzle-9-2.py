def getArea(pointA, pointB):
    ax, ay = pointA
    bx, by = pointB
    return (abs(ax - bx) + 1) * (abs(ay - by) + 1)


def buildEdges(points):
    edges = []
    n = len(points)
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]  # wrap around
        edges.append((p1, p2))
    return edges


def edgeCrossesRectangle(edge, r1, r2):
    (ex1, ey1), (ex2, ey2) = edge
    rx1, ry1 = r1
    rx2, ry2 = r2

    minX = min(rx1, rx2)
    maxX = max(rx1, rx2)
    minY = min(ry1, ry2)
    maxY = max(ry1, ry2)

    if minX == maxX or minY == maxY: #single line rectange
        return False

    # Vertical edge
    if ex1 == ex2:
        ex = ex1
        eyMin = min(ey1, ey2)
        eyMax = max(ey1, ey2)

        # Edge must be strictly inside horizontally
        if not (minX < ex < maxX):
            return False

        # Overlap of y-intervals with positive length
        overlapLow = max(eyMin, minY)
        overlapHigh = min(eyMax, maxY)
        return overlapLow < overlapHigh

    # Horizontal edge
    if ey1 == ey2:
        ey = ey1
        exMin = min(ex1, ex2)
        exMax = max(ex1, ex2)

        # Edge must be strictly inside vertically
        if not (minY < ey < maxY):
            return False

        overlapLeft = max(exMin, minX)
        overlapRight = min(exMax, maxX)
        return overlapLeft < overlapRight

    return False


def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()

    points = []
    for line in lines:
        x_str, y_str = line.strip().split(",")
        points.append((int(x_str), int(y_str)))

    n = len(points)
    edges = buildEdges(points)

    maximum = 0

    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            area = getArea(p1, p2)
            if area <= maximum:
                continue 

            valid = True
            for e in edges:
                if edgeCrossesRectangle(e, p1, p2):
                    valid = False
                    break

            if valid:
                maximum = area

    print(maximum)


main()
