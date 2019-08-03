import numpy as np
check=0

array=np.zeros((19,19))

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs():
    for x in range(19):
        for y in range(19):
            if array[y][x] != 0:
                color = array[y][x] # int
                for i in range(4):
                    distance = 0
                    j = 1
                    while 0 <= y+dy[i]*j < 19 and 0 <= x+dx[i]*j < 19 and array[y+dy[i]*j][x+dx[i]*j] == color:
                        distance += 1
                        j += 1

                    j = 1
                    while 0 <= y+dy[i+4]*j < 19 and 0 <= x+dx[i+4]*j < 19 and array[y+dy[i+4]*j][x+dx[i+4]*j] == color:
                        distance += 1
                        j += 1

                    if distance == 4:
                        print(color)
                        return color
                   
                       
check == False
while check == False:
    a,xpos,ypos = input().split(',')
    a=int(a)
    xpos=int(xpos)
    ypos=int(ypos)
    #a = int(input("B or W?"))
    #xpos = int(input("X position"))
    #ypos= int(input("Y position"))
    if a==1000 :
        array[ypos][xpos]=1
        Data=[array]
        if dfs(): check = True
    
    else :
        array[ypos][xpos]=2
        Data=[array]
        if dfs(): check = True