def process(ln):
    rs, re = ln.split("-")
    return((int(rs), int(re)))

def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        n = 0
        ranges = []
        
        for ln in lines:
            if(ln == "\n"):
                break
            ln = ln.replace("\n", "", 1)
            ranges.append(process(ln))
        ranges.sort()

        for i in range(len(ranges)):
            rs1, re1 = ranges[i]
            if(rs1 == -1 and re1 == -1):
                continue
            n = n + re1 - rs1 + 1

            for j in range(i + 1, len(ranges)):
                rs2, re2 = ranges[j]
                if(rs2 == -1 and re2 == -1):
                    continue
                # the second range start within first range but ends outside of first range
                if( rs2 >= rs1 and rs2 <= re1 and re2 > re1):
                    ranges[j] = (re1 + 1, re2)
                # the second range is completely within the first range
                elif(rs2 >= rs1 and rs2 <= re1 and re2 <= re1):
                    ranges[j] = (-1, -1)
                # the second range is completely outside and before the first range
                elif(rs2 > rs1 and rs2 > re1):
                    continue        
        
        print(n)    
main()