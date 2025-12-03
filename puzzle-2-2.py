import math
def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        total = 0
        dic = {}
        for ln in lines:
            ln = ln.replace("\n", "", 1)
            ln = ln.split(",")
            
            for r in ln:
                rs, re = r.split("-")
                
                rs = int(rs)
                re = int(re)

                while(rs <= re):
                    b = str(rs)
                    maxMLen = len(b)//2
                    
                    m = ""
                    for i in range(maxMLen):
                        m = b[:i+1]
                        
                        x = b.count(m)   
                        
                        if(x*len(m) == len(b)):
                            print(b, "is made of", m)
                            if(int(b) not in dic):
                                total = total + int(b)
                                dic[int(b)] = 1

                    rs = rs + 1
        print("Final total:", total)
main()

