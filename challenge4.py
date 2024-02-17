def generate_maze(n, m, hints):
    maze = [[0] * m for _ in range(n)]
    
    for i in range(len(hints)):
        for j in range(len(hints[0])):
            hint = hints[i][j]
            moves = sum(hint)-hint[0]
            moves = moves % 4
            if hint[0] == 1:
                if moves == 1 or moves == -3:
                    maze[i*2][j*2+1] =1
                elif moves == 2 or moves == -2:
                    maze[i*2][j*2] =1
                elif moves == 3 or moves == -1:
                    maze[i*2+1][j*2] =1
                elif moves == 0 :
                    maze[i*2+1][j*2+1] =1
            elif hint[0] == 2:
                if moves == 1 or moves == -3:
                    maze[i*2][j*2] =1
                    maze[i*2+1][j*2] =1
                elif moves == 2 or moves == -2:
                    maze[i*2+1][j*2+1] =1
                    maze[i*2+1][j*2] =1
                elif moves == 3 or moves == -1:
                    maze[i*2][j*2+1] =1
                    maze[i*2+1][j*2+1] =1
                elif moves == 0 :
                    maze[i*2][j*2] =1
                    maze[i*2][j*2+1] =1
            elif hint[0] == 3:
                if moves == 1 or moves == -3:
                    maze[i*2][j*2+1] =1
                    maze[i*2][j*2] =1
                    maze[i*2+1][j*2+1] =1
                elif moves == 2 or moves == -2:
                    maze[i*2][j*2+1] =1
                    maze[i*2][j*2] =1
                    maze[i*2+1][j*2] =1
                elif moves == 3 or moves == -1:
                    maze[i*2+1][j*2] =1
                    maze[i*2][j*2] =1
                    maze[i*2+1][j*2+1] =1
                elif moves == 0 :
                    maze[i*2][j*2+1] =1
                    maze[i*2+1][j*2] =1
                    maze[i*2+1][j*2+1] =1
    
    return maze


def parseHints(hints):
    newHints = []
    for x in hints :
        newLine = []
        for y in x : 
            splited = y.split(',')
            #print(splited)
            arr = []
            arr.append(int(splited[0]))
            for _,e in enumerate(splited) :
                if (_ == 0) :
                    continue
                else :
                    if(e == 'r'):
                        arr.append(-1)
                    elif(e == 'l'):
                        arr.append(1)
                    else:
                        print('there might be a typo')
            newLine.append(arr)
        newHints.append(newLine)
    return newHints

# Example usage
n = 6
m = 6

#R = -1 , L = 1
#same position = 4*k
hints = [
    ["2", "3,l", "1,l,l"],
    ["1,r","2,r,r", "3"],
    ["1,l,l", "3", "2,r"]
]

newHints = parseHints(hints= hints)
maze = generate_maze(n, m, newHints)
for row in maze:
    print(' '.join(map(str, row)))
