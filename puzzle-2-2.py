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
                # rs = range start, re = range end
                rs = int(rs)
                re = int(re)

                while(rs <= re):
                    b = str(rs)
                    # maximum length of the repeating pattern is half of the string length
                    maxMLen = len(b)//2
                    
                    m = ""
                    # creating a substring from the beginning of b for each of the length till maxMLen and checking if the actual string 
                    # is made of the substring m
                    for i in range(maxMLen):
                        m = b[:i+1]
                        
                        # checking how many times that substring appears in the actual string
                        x = b.count(m)   
                        
                        # length of m * number of times it appears on the string should be equal to the actual string length for that to be an invalid ID.
                        if(x*len(m) == len(b)):
                            print(b, "is made of", m)
                            # to avoid counting 222222 for 2, 22, 222 patterns. We should count this once.
                            if(int(b) not in dic):
                                total = total + int(b)
                                dic[int(b)] = 1

                    rs = rs + 1
        print("Final total:", total)
main()

