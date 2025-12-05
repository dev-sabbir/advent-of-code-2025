def process(ln):
    range_start, range_end = ln.split("-")
    return((int(range_start), int(range_end)))

def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        result = 0
        ranges = []
        ingredients = []
        
        flag = 0
        for ln in lines:
            if(ln == "\n"):
                flag = 1
                continue
            
            ln = ln.replace("\n", "", 1)

            if(not flag):    
                ranges.append(process(ln))        
            else:
                ingredients.append(int(ln))
        print("length of ranges:", len(ranges))
        
        for ingId in ingredients:
            for (range_start, range_end) in ranges:
                if(ingId >= range_start and ingId <= range_end):
                    result = result + 1
                    break
        print(result)    
main()