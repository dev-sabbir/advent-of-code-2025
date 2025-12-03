import math
def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        total = 0
        for ln in lines:
            ln = ln.replace("\n", "", 1)
            ln = ln.split(",")
            print(ln)
            for r in ln:
                rs, re = r.split("-")
                
                rs = int(rs)
                re = int(re)

                while(rs <= re):
                    b = str(rs)
                    if(len(b) > 1 and len(b)%2 == 0):
                        b1 = b[int(len(b)/2): ]
                        b2 = b[ :int(len(b)/2)]
                        
                        b1 = int(b1)
                        b2 = int(b2)
                        if(b1 == b2):
                            print("b:", b)
                            total = total + int(b)
                    rs = rs + 1
        print("Final total:", total)
main()

