import numpy as np
array=np.zeros((20,20))

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


global coun
coun=0

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

                 
def ccheck_up(current_color,cur_xpos,cur_ypos):  #위쪽방향 탐색
    blank=0
    ccolor=0
    global coun
    for num1 in range(1,4):        

        if current_color == 1000:
            if array[cur_ypos-num1][cur_xpos] == 2 and cur_ypos-num1 >0:
                break
            elif array[cur_ypos-num1][cur_xpos] ==0 and cur_ypos-num1 >0:
                blank+=1
            elif cur_ypos-num1 >0:
                ccolor+=1
        
        else:
            if array[cur_ypos-num1][cur_xpos] == 1 and cur_ypos-num1 >0:
                break
            elif array[cur_ypos-num1][cur_xpos] ==0 and cur_ypos-num1 >0:
                blank+=1
            elif cur_ypos-num1 >0:
                ccolor+=1
        if blank ==2:
            break
        if ccolor>1: # or ccolor + blank==3
            coun+=1
            break

def ccheck_upright(current_color,cur_xpos,cur_ypos):  #오른쪽 위 방향 탐색
    blank=0
    ccolor=0
    global coun
    for num1 in range(1,4):        

        if current_color == 1000:
            if array[cur_ypos-num1][cur_xpos+num1] == 2 and cur_ypos-num1 >0 and cur_xpos+num1<20:
                break
            elif array[cur_ypos-num1][cur_xpos+num1] ==0 and cur_ypos-num1 >0 and cur_xpos+num1<20:
                blank+=1
            elif cur_ypos-num1 >0 and cur_xpos+num1<20:
                ccolor+=1
        
        else:
            if array[cur_ypos-num1][cur_xpos+num1] == 1 and cur_ypos-num1 >0 and cur_xpos+num1<20:
                break
            elif array[cur_ypos-num1][cur_xpos+num1] ==0 and cur_ypos-num1 >0 and cur_xpos+num1<20:
                blank+=1
            elif cur_ypos-num1 >0 and cur_xpos+num1<20:
                ccolor+=1
        if blank ==2:
            break
        if ccolor>1: # or ccolor + blank==3:
            coun+=1
            break

def ccheck_right(current_color,cur_xpos,cur_ypos):  #오른쪽 방향 탐색
    blank=0
    ccolor=0
    
    global coun
    for num1 in range(1,4):        

        if current_color == 1000:
            if array[cur_ypos][cur_xpos+1] == 2 and cur_xpos+num1<20:
                break
            elif array[cur_ypos][cur_xpos+1] ==0 and cur_xpos+num1<20:
                blank+=1
            elif cur_ypos-num1 >0 and cur_xpos+1<20:
                ccolor+=1
        
        else:
            if array[cur_ypos][cur_xpos+1] == 1  and cur_xpos+num1<20:
                break
            elif array[cur_ypos][cur_xpos+1] ==0 and cur_xpos+num1<20:
                blank+=1
            elif cur_xpos+1<20:
                ccolor+=1
        if blank ==2:
            break
        if ccolor>1: # or ccolor + blank==3:
            coun+=1
            break

def ccheck_downright(current_color,cur_xpos,cur_ypos):  #오른쪽 아래 방향 탐색
    blank=0
    ccolor=0
    global coun
    for num1 in range(1,4):        

        if current_color == 1000:
            if array[cur_ypos+num1][cur_xpos+num1] == 2 and cur_ypos+num1 <20 and cur_xpos+num1<20:
                break
            elif array[cur_ypos+num1][cur_xpos+num1] ==0 and cur_ypos+num1 <20 and cur_xpos+num1<20:
                blank+=1
            elif cur_ypos +num1 <20 and cur_xpos+num1<20:
                ccolor+=1
        
        else:
            if array[cur_ypos+num1][cur_xpos+num1] == 1 and cur_ypos+num1 <20 and cur_xpos+num1<20:
                break
            elif array[cur_ypos+num1][cur_xpos+num1] ==0 and cur_ypos+num1 <20 and cur_xpos+num1<20:
                blank+=1
            elif cur_ypos+num1 <20 and cur_xpos+num1<20:
                ccolor+=1
        if blank ==2:
            break
        if ccolor>1: # or ccolor + blank==3:
            coun+=1
            break

def ccheck_down(current_color,cur_xpos,cur_ypos):  #아래 방향 탐색
    blank=0
    global coun
    ccolor=0
    for num1 in range(1,4):        

        if current_color == 1000:
            if array[cur_ypos+num1][cur_xpos] == 2 and cur_ypos+num1 <20 :
                break
            elif array[cur_ypos+num1][cur_xpos] ==0 and cur_ypos+num1 <20 :
                blank+=1
            elif cur_ypos +num1 <20 :
                ccolor+=1
        
        else:
            if array[cur_ypos+num1][cur_xpos] == 1 and cur_ypos+num1 <20 :
                break
            elif array[cur_ypos+num1][cur_xpos] ==0 and cur_ypos+num1 <20 :
                blank+=1
            elif cur_ypos+num1 <20:
                ccolor+=1
        if blank ==2:
            break
        if ccolor>1 :# or ccolor + blank==3:
            coun+=1
            break


def ccheck_downleft(current_color,cur_xpos,cur_ypos):  #왼쪽 아래 방향 탐색
    blank=0
    ccolor=0
    global coun
    for num1 in range(1,4):        

        if current_color == 1000:
            if array[cur_ypos+num1][cur_xpos-num1] == 2 and cur_ypos+num1 <20 and cur_xpos-num1>0:
                break
            elif array[cur_ypos+num1][cur_xpos-num1] ==0 and cur_ypos+num1 <20 and cur_xpos-num1>0:
                blank+=1
            elif cur_ypos +num1 <20 and cur_xpos-num1>0:
                ccolor+=1
        
        else:
            if array[cur_ypos+num1][cur_xpos-num1] == 1 and cur_ypos+num1 <20 and cur_xpos-num1>0:
                break
            elif array[cur_ypos+num1][cur_xpos-num1] ==0 and cur_ypos+num1 <20 and cur_xpos-num1>0:
                blank+=1
            elif cur_ypos+num1 <20 and cur_xpos-num1>0:
                ccolor+=1
        if blank ==2:
            break
        if ccolor>1: # or ccolor + blank==3:
            coun+=1
            break

def ccheck_left(current_color,cur_xpos,cur_ypos):  #왼쪽 방향 탐색
    blank=0
    ccolor=0
    global coun
    for num1 in range(1,4):        

        if current_color == 1000:
            if array[cur_ypos][cur_xpos-num1] == 2 and cur_xpos-num1>0:
                break
            elif array[cur_ypos][cur_xpos-num1] ==0 and cur_xpos-num1>0:
                blank+=1
            elif  cur_xpos-num1>0:
                ccolor+=1

        
        else:
            if array[cur_ypos][cur_xpos-num1] == 1 and cur_xpos-num1>0:
                break
            elif array[cur_ypos][cur_xpos-num1] ==0and cur_xpos-num1>0:
                blank+=1
            elif  cur_xpos-num1>0:
                ccolor+=1
        if blank ==2:
            break
        if ccolor>1: #or ccolor + blank==3:
            coun+=1
            break


def ccheck_upleft(current_color,cur_xpos,cur_ypos):  #왼쪽위 방향 탐색
    blank=0
    ccolor=0
    global coun
    for num1 in range(1,4):        

        if current_color == 1000:
            if array[cur_ypos-num1][cur_xpos-num1] == 2 and cur_ypos-num1>0 and cur_xpos-num1>0:
                break
            elif array[cur_ypos-num1][cur_xpos-num1] ==0 and cur_ypos-num1 >0 and cur_xpos-num1>0:
                blank+=1
            elif cur_ypos -num1 >0 and cur_xpos-num1>0:
                ccolor+=1
        
        else:
            if array[cur_ypos-num1][cur_xpos-num1] == 1 and cur_ypos-num1 >0 and cur_xpos-num1>0:
                break
            elif array[cur_ypos-num1][cur_xpos-num1] ==0 and cur_ypos-num1 >0 and cur_xpos-num1>0:
                blank+=1
            elif cur_ypos-num1 >0 and cur_xpos-num1>0:
                ccolor+=1
        if blank ==2:
            break
        if ccolor>1: # or ccolor + blank==3:
            coun+=1
            break

                      
check = False
while check == False:
    coun=0
    a,xpos,ypos = input().split(',')
    a=int(a)
    xpos=int(xpos)
    ypos=int(ypos)
    ccheck_down(a,xpos,ypos)
    ccheck_downleft(a,xpos,ypos)
    ccheck_downright(a,xpos,ypos)
    ccheck_left(a,xpos,ypos)
    ccheck_right(a,xpos,ypos)
    ccheck_up(a,xpos,ypos)
    ccheck_upleft(a,xpos,ypos)
    ccheck_upright(a,xpos,ypos)
    print(coun)

    if coun>=2:
        print('안됨')
        
        continue
       
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

    