def prepareGraph(lines):
    edges = {}
    for line in lines:
        vIn = line[0].strip(":")
        
        for i in range(1, len(line)):
        
            if(vIn not in edges):
                edges[vIn] = []
            edges[vIn].append(line[i])

    return edges

def dfs(edges, current, end, memo):
    key = (current, end)
    if key in memo:
        return memo[key]

    if current == end:
        return 1

    total = 0

    for neighbor in edges.get(current, []):
        total += dfs(edges, neighbor, end, memo)

    memo[key] = total
    return total
    
def main():
    total = 0
    filepath = "input.txt"

    start = "svr"
    fft = "fft"
    dac = "dac"
    end  = "out"
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
        i = 0
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "", 1).split(" ")
        
        edges = prepareGraph(lines)
        memo = {}

        svr_to_dac = dfs(edges, start, dac, memo)
        dac_to_fft = dfs(edges, dac, fft, memo)
        fft_to_out = dfs(edges, fft, end, memo)

        svr_to_fft = dfs(edges, start, fft, memo)
        fft_to_dac = dfs(edges, fft, dac, memo)
        dac_to_out = dfs(edges, dac, end, memo)

        total = (svr_to_dac * dac_to_fft * fft_to_out) + (svr_to_fft * fft_to_dac * dac_to_out)
        
        print(total)
main()