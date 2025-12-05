def process(ln):
    rs, re = ln.split("-")
    return((int(rs), int(re)))

def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        n = 0
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
            for (rs, re) in ranges:
                if(ingId >= rs and ingId <= re):
                    n = n + 1
                    break
        print(n)    
main()