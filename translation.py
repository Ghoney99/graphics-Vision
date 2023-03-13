import numpy as np
import turtle as t

t.hideturtle()      #펜포인터 숨기기
t.penup()           #펜 들기 (그리지 않음)

def midpointLine(x0,y0,x1,y1) : #Midpoint Line Drawing 알고리즘
    dx=x1-x0
    dy=y1-y0
    t.penup()
    t.goto(x0,y0)
    t.pendown()
    if(dx>dy) :     #기울기가 1보다 작을때 (m<1)
        d=dy*2-dx
        incrE=dy*2
        incrNE=(dy-dx)*2
        x=x0
        y=y0
        while(x<x1):
            if(d<=0):
                d=incrE+d
                x=x+1
            else:
                d=d+incrNE
                x=x+1
                y=y+1
            t.goto(x,y)
    
    else :          #기울기가 1보다 클때 (m>1)
        d=dx*2-dy
        incrE=dx*2
        incrNE=(dx-dy)*2
        x=x0
        y=y0
        while(y<y1):
            if(d<=0):
                d=incrE+d
                y=y+1
            else:
                d=d+incrNE
                x=x+1
                y=y+1
            t.goto(x,y)
    t.penup()

def Translation(x,y,dx,dy) : 
    T = np.array([[1,0,dx],[0,1,dy],[0,0,1]])
    P = np.array([[x],[y],[1]])
    newP =T@P
    return newP


def drawline(x1,y1,x2,y2):  #선분을 그리는 함수
    t.speed(0)
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)


drawline(-500,0,500,0)  #좌표계를 그리는 작업
drawline(0,-500,0,500)
t.penup()


x0_input = int(input("시작점의 x,y좌표를 입력하세요 : "))
y0_input = int(input(""))
x1_input = int(input("끝점의 x,y좌표를 입력하세요 : "))
y1_input = int(input(""))

t.speed(0)
t.goto(x0_input,y0_input)
t.pendown()
midpointLine(x0_input,y0_input,x1_input,y1_input)
t.penup()

x2_input = int(input("옮길 좌표의 값만큼 x,y를 입력하세요 : "))
y2_input = int(input(""))
mat1=Translation(x0_input,y0_input,x2_input,y2_input)
mat2=Translation(x1_input,y1_input,x2_input,y2_input)
midpointLine(mat1[0][0],mat1[1][0],mat2[0][0],mat2[1][0])

t.mainloop()
