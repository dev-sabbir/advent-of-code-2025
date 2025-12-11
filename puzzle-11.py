def prepareGraph(lines):
    vertices = []
    edges = {}
    for line in lines:
        vIn = line[0].strip(":")
        vertices.append(vIn)
        for i in range(1, len(line)):
            vertices.append(line[i])
            if(vIn not in edges):
                edges[vIn] = []
            edges[vIn].append(line[i])

    vertices = set(vertices)
    vertices = list(vertices)
    return (vertices, edges)

def solve(vertices, edges):
    start = "you"
    end  = "out"
    count = 0
    visited = {}
    q = [start]

    while(len(q) > 0):
        curr = q.pop(0)

        for v in edges[curr]:
            if(v == end):
                count += 1
            else:
                q.append(v)
    
    return count
        
            

def main():
    total = 0
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        i = 0
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "", 1).split(" ")
        
        vertices, edges = prepareGraph(lines)
        print(vertices, edges)

        total = solve(vertices, edges)
        print(total)
main()