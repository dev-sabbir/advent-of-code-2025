def doMath(a, b, sign):
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
        res = []

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if(i == 0):
                    res.append(lines[i][j])
                else:
                    if(lines[i][j] >= '0' and lines[i][j] <= '9'):
                        if(res[j] != ' '):
                            res[j] = int(res[j]) * 10 + int(lines[i][j])
                        else:
                            res[j] = 0
                            res[j] = int(res[j]) * 10 + int(lines[i][j])

        tempTotal = 0
        total = 0
        for i in range(len(res) -1):
            if(lines[len(lines)-1][i] != ' '):
                sign = lines[len(lines)-1][i]
                total = total + tempTotal
                tempTotal = 1 if sign == '*' else 0
            if(res[i] != ' ' and res[i] != '\n'):
                tempTotal = doMath(res[i], tempTotal, sign)
        total = total + tempTotal
        print('res by sol2: ', total)
            


main()