def process(ln):
    range_start, range_end = ln.split("-")
    return((int(range_start), int(range_end)))

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
            range_start1, range_end1 = ranges[i]
            if(range_start1 == -1 and range_end1 == -1):
                continue
            n = n + range_end1 - range_start1 + 1

            for j in range(i + 1, len(ranges)):
                range_start2, range_end2 = ranges[j]
                if(range_start2 == -1 and range_end2 == -1):
                    continue
                # the second range start within first range but ends outside of first range
                if( range_start2 >= range_start1 and range_start2 <= range_end1 and range_end2 > range_end1):
                    ranges[j] = (range_end1 + 1, range_end2)
                # the second range is completely within the first range
                elif(range_start2 >= range_start1 and range_start2 <= range_end1 and range_end2 <= range_end1):
                    ranges[j] = (-1, -1)
                # the second range is completely outside and before the first range
                elif(range_start2 > range_start1 and range_start2 > range_end1):
                    continue        
        
        print(n)    
main()