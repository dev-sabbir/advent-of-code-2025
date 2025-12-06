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
            lines[i] = lines[i].replace("\n", "", 1)
        
        signsRow = len(lines) - 1
        result = []
        sign = ''
        r = -1
        for j in range(len(lines[0])):
            
            if(lines[signsRow][j] != ' '):
                if(sign != ''):
                    result[r].append(sign)
                sign = lines[signsRow][j]
                result.append([])
                r = r + 1
            num = 0
            for i in range(len(lines) - 1):
                if(lines[i][j] != ' '):
                    num = num * 10 + int(lines[i][j])
            if(num > 0):
                result[r].append(num)
        if(sign != ''):
            result[r].append(sign)
        print(result)

        total = 0
        for resultRow in result:
            temp = resultRow[0]
            sign = resultRow[len(resultRow) -1]
            for i in range(1, len(resultRow) -1):
                temp = doMath(resultRow[i], temp, sign)
            total = total + temp
        print(total)
        
main()