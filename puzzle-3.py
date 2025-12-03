import math
def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        n = 0
        for ln in lines:
            ln = ln.replace("\n", "", 1)
            f,s = ln[0], ln[1]
            
            for i,val in enumerate(ln):
                if(i >= 1):
                    if(val > f and i < len(ln) - 1):
                        f = val
                        
                        s = ln[i+1]
                        
                    elif(val > s):
                        s = val
                        
            z = int(f) * 10 + int(s)
            print("z: ", z)
            n = n + z
        print(n) 
main()