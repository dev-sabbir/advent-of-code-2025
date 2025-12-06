def doMath(a, b, sign):
    print(f"Calculating: {a} {sign} {b}")
    a = int(a)
    b = int(b)
    
    if sign == "+":
        return a + b
    else:
        return a * b

def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "", 1).split(" ")
            lines[i] = [s for s in lines[i] if s != ""]
        
        result = lines[0]
        signs = lines[len(lines)-1]

        for i in range(1, len(lines)-1):
            for j in range(len(lines[i])):
                result[j] = doMath(result[j], lines[i][j], signs[j])
        
        sum = 0
        for num in result:
            sum += int(num)

        print(sum)

main()