import math
def main():
    filepath = "input.txt"
    curr = 50
    count = 0
    with open(filepath, 'r') as file:
        lines = file.readlines()
        x = 1
        for ln in lines:
            total = 0
            ln = ln.replace("\n", "", 1)

            dir = ln[:1]
            dist = int(ln[1:])
            print("dir:", dir, "dist:", dist)
            total = math.floor(dist/100)
            dist = dist%100
            print("new dist:", dist)
            if(dir == "L"):
                prevCurr = curr
                curr = curr - dist
                print("curr:", curr)
                if(curr < 0):
                    if(prevCurr > 0):
                        total = total + 1
                    curr = curr%100
            if(dir == "R"):
                curr = curr + dist
                print("curr:", curr)
                if(curr > 100):
                    total = total + 1
                    curr = curr%100
            count = count + total
            if(curr == 0 or curr == 100):
                count = count+1
                curr = 0
            print("total:", total, "count:", count, "curr:", curr)
    print("Final position:", count)       
main()