def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        total = 0

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if(lines[i][j] == 'S'):
                    if(i < len(lines) -1):
                        if(lines[i+1][j] == '.'):
                            lines[i+1] = lines[i+1][:j] + 'S' + lines[i+1][j + 1:]
                if(lines[i][j] == '^'):
                    if(i > 0):
                        if(lines[i-1][j] == 'S' and i < len(lines) - 1):
                            total += 1
                            lines[i+1] = lines[i+1][:j-1] + 'S' + lines[i+1][j:]
                            lines[i+1] = lines[i+1][:j+1] + 'S' + lines[i+1][j+2:]
        print(lines)
        print("total:", total)        


main()