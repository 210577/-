from functions import *
from turtle import *
from math import *

k=0
print("=============================================")
print("         그래프 그리기 프로그램 v4.0 - 19152 임지안       ")
print("=============================================")
while True:
    print("그리고 싶은  함수의 종류를 아래와 같이 입력해주세요.")
    func = input("다항함수: 1, 무리함수: 2, 유리함수: 3")
    try:
        if int(func) < 4 and int(func) > 0:
            break
    except:
        break

if func == '1':
    A = polynomial(0,[])
    tier = A[0]
    arr = A[1]
    def ef(x):
        global tier
        global arr
        k = tier
        result = 0
        while k >= 0:
            a = x**k
            result += a * float(arr[k])
            k -= 1
        return result
elif func == '2':
    B = irrational(0,0,0,0)
    def ef(x):
        return B[0] * sqrt(B[1]*x + B[2]) + B[3]
elif func == '3':
    C = rational(0,0,0,0)
    def ef(x):
        global k
        try:
            k = -1*C[3]/C[2]
            a = ((C[0]*x + C[1])/(C[2]*x+C[3]))
        except:
            a =  9999999999
        return a

title("만능 그래프 그리기 v2.0")
setup(width = 900,height = 900)
speed(0)
for i in (90,180,270,360):
    fd(450)
    goto(0,0)
    setheading(i)
goto(0,0)
pencolor('red')
penup()


if func == '1':
    goto(200,0)
    write("200")
    goto(0,200)
    write("200")
    goto(-200,0)
    write("-200")
    goto(0,-200)
    write("-200")
    goto(-900,ef(-900))
    pendown()
    for i in range(-900,900):
        goto(i,ef(i))
elif func == '2':
    goto(200,0)
    write("200")
    goto(0,200)
    write("200")
    goto(-200,0)
    write("-200")
    goto(0,-200)
    write("-200")
    for i in range(-900,900):
        try:
            goto(i,ef(i))
            pendown()
        except:
            continue
elif func == '3':
    goto(225,0)
    write("5")
    goto(0,225)
    write("5")
    goto(-225,0)
    write("-5")
    goto(0,-225)
    write("-5")
    for i in range(-900,900):
        try:
            speed(5)

            if abs(ef(i/45)) >= 20:
                penup()
                continue
            else:
                goto(i,45*ef(i/45))
                pendown()
        except:
            penup()
            speed(0)
            continue

