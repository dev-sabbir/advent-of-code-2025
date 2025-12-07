def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        
        W = max(len(line) for line in lines)

        #finding the starting poing
        for r, row in enumerate(lines):
            c = row.find("S")
            if c != -1:
                start = (r, c)
                break

        sr, sc = start
        
        splitterRowsForColumn = [[] for _ in range(W)]
        for r in range(len(lines)):
            for c, ch in enumerate(lines[r]):
                if ch == "^":
                    splitterRowsForColumn[c].append(r)
        

        def splitterRowBelow(r, c):
            rows = splitterRowsForColumn[c]
            for i in range(len(rows)):
                if(rows[i] > r):
                    return rows[i]
            return None

        def getTimelines(r, c, memo):
            key = (r, c)
            if key in memo:
                return memo[key]

            # we are out of the grid - horizontally
            if c < 0 or c >= W:
                memo[key] = 1
                return 1

            rs = splitterRowBelow(r, c)
            # we are outside of the grid - vertically
            if rs is None:
                memo[key] = 1
                return 1

            memo[key] = getTimelines(rs, c - 1, memo) + getTimelines(rs, c + 1, memo)
            return memo[key]
        
        print(getTimelines(sr, sc, {}))
main()