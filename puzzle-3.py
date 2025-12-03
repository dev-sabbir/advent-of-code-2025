import math
def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        n = 0
        for ln in lines:
            ln = ln.replace("\n", "", 1)
            # default first and second digit
            f,s = ln[0], ln[1]
            
            for i,val in enumerate(ln):
                if(i >= 1):
                    # the first digit should not be the last item of the string
                    if(val > f and i < len(ln) - 1):
                        f = val
                        # once we have the first digit, the second digit will be at least the next index.
                        s = ln[i+1]
                        
                    elif(val > s):
                        s = val
            # creating a two-digit number from the two individual digits            
            z = int(f) * 10 + int(s)
            print("z: ", z)
            n = n + z
        print(n) 
main()