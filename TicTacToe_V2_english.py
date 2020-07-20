import turtle as t

#------------------#
actualX = 0
actualY = 0
answer = 0

current_pos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
possible_wins_results = []
win = 0
draw = 0

i = 0
#------------------#
def checkWinFor(x, y, z):
    if (current_pos[int(x-1)] == current_pos[int(y-1)] == current_pos[int(z-1)]):
        return current_pos[int(x-1)]
    else:
        return 0

def CheckForWin():
    win = 0
    possible_wins_results = []
    possible_wins_results.append(checkWinFor(1, 2, 3))
    possible_wins_results.append(checkWinFor(4, 5, 6))
    possible_wins_results.append(checkWinFor(7, 8, 9))
    possible_wins_results.append(checkWinFor(1, 4, 7))
    possible_wins_results.append(checkWinFor(2, 5, 8))
    possible_wins_results.append(checkWinFor(3, 6, 9))
    possible_wins_results.append(checkWinFor(1, 5, 9))
    possible_wins_results.append(checkWinFor(7, 5, 3))
    i = 0
    while i<8:
        if possible_wins_results[i]==1:
            win = 1
        if possible_wins_results[i]==2:
            win = 2
        i = i+1
    return win

def checkForDraw():
    i = 0
    draw = 1
    while i<8:
        if current_pos[i] ==0:
            draw = 0
        i = i + 1
    return draw
    

def gotoNumberPosition():
    t.setheading(90)
    t.fd(10)
    t.setheading(180)
    t.fd(10)
    t.setheading(0)
    
def drawBoard():
    t.pd()
    t.goto(300, 0)
    t.goto(300, 300)
    t.goto(0, 300)
    t.goto(0, 0)
    t.goto(100, 0)
    t.goto(100, 300)
    t.goto(200, 300)
    t.goto(200, 0)
    t.pu()
    t.goto(300, 100)
    t.pd()
    t.goto(0, 100)
    t.goto(0, 200)
    t.goto(300, 200)
    t.pu()
    t.home()

def drawNumbers():
    t.color('grey')
    t.pu()
    
    t.goto(100, 200)
    gotoNumberPosition()
    t.setheading(90)
    t.pd()
    t.fd(20)
    t.pu()

    t.goto(200, 200)
    gotoNumberPosition()
    t.pd()
    t.setheading(180)
    t.fd(10)
    t.setheading(90)
    t.fd(10)
    t.setheading(0)
    t.fd(10)
    t.setheading(90)
    t.fd(10)
    t.setheading(180)
    t.fd(10)
    t.pu()

    t.goto(300, 200)
    gotoNumberPosition()
    t.setheading(180)
    t.pd()
    t.fd(10)
    t.bk(10)
    t.setheading(90)
    t.fd(10)
    t.setheading(180)
    t.fd(10)
    t.bk(10)
    t.setheading(90)
    t.fd(10)
    t.setheading(180)
    t.fd(10)
    t.pu()

    t.goto(100, 100)
    gotoNumberPosition()
    t.setheading(90)
    t.pd()
    t.fd(20)
    t.bk(10)
    t.setheading(180)
    t.fd(10)
    t.setheading(90)
    t.fd(10)
    t.pu()

    t.goto(200, 100)
    gotoNumberPosition()
    t.setheading(180)
    t.pd()
    t.fd(10)
    t.bk(10)
    t.setheading(90)
    t.fd(10)
    t.setheading(180)
    t.fd(10)
    t.setheading(90)
    t.fd(10)
    t.setheading(0)
    t.fd(10)
    t.pu()

    t.goto(300, 100)
    gotoNumberPosition()
    t.setheading(180)
    t.pd()
    t.fd(10)
    t.setheading(90)
    t.fd(20)
    t.setheading(0)
    t.fd(10)
    t.bk(10)
    t.setheading(90)
    t.bk(10)
    t.setheading(0)
    t.fd(10)
    t.setheading(270)
    t.fd(10)
    t.pu()

    t.goto(100, 0)
    gotoNumberPosition()
    t.pd()
    t.setheading(90)
    t.fd(20)
    t.setheading(180)
    t.fd(10)
    t.pu()

    t.goto(200, 0)
    gotoNumberPosition()
    t.pd()
    t.setheading(180)
    t.fd(10)
    t.setheading(90)
    t.fd(20)
    t.setheading(0)
    t.fd(10)
    t.setheading(270)
    t.fd(10)
    t.setheading(180)
    t.fd(10)
    t.bk(10)
    t.setheading(270)
    t.fd(10)
    t.pu()

    t.goto(300, 0)
    gotoNumberPosition()
    t.pd()
    t.setheading(180)
    t.fd(10)
    t.bk(10)
    t.setheading(90)
    t.fd(20)
    t.setheading(180)
    t.fd(10)
    t.setheading(270)
    t.fd(10)
    t.setheading(0)
    t.fd(10)

def drawSign(x, y, color):
    if x>3:
        print('ERROR, X VALUE TOO HIGH')
    if y>3:
        print('ERROR, Y VALUE TOO HIGH')
    if x<=0:
        print('ERROR, X VALUE TOO LOW')
    if y<=0:
        print('ERROR, Y VALUE TOO LOW')
    actualX = (x * 100)-50
    actualY = (y * 100)-75
    t.pu()
    t.goto(actualX, actualY)
    t.pd()
    t.begin_fill()
    t.color(color)
    t.circle(30)
    t.end_fill()
    t.pu()
    t.home()

def drawSignNumber(number, color):
    if float(number) == 1:
        drawSign(1, 3, color)
    if float(number) == 2:
        drawSign(2, 3, color)
    if float(number) == 3:
        drawSign(3, 3, color)
    if float(number) == 4:
        drawSign(1, 2, color)
    if float(number) == 5:
        drawSign(2, 2, color)
    if float(number) == 6:
        drawSign(3, 2, color)
    if float(number) == 7:
        drawSign(1, 1, color)
    if float(number) == 8:
        drawSign(2, 1, color)
    if float(number) == 9:
        drawSign(3, 1, color)

#1 = red, 2 = yellow
def askMove(Team):
    if float(Team) == 1:
        print('Team rood:')
    elif Team == 2:
        print('Team geel:')

    answer = float(input('kies een vak ->'))
    if current_pos[(int(answer))-1] == 0:
        current_pos[(int(answer))-1] = Team
        if Team == 1:
            drawSignNumber(answer, 'red3')
        elif Team == 2:
            drawSignNumber(answer, 'gold')
    else:
        print('Jammer, dit vak is al bezet. ronde verloren')
    print('---------------------------')
    

#------------------#
t.title('tic tac toe')
win = 0
t.speed(100)
t.hideturtle()
drawBoard()
drawNumbers()

while True:
    askMove(1)
    win = CheckForWin()
    if win == 1:
        print('rood heeft gewonnen')
        break
    draw = checkForDraw()
    if draw == 1:
        print('Gelijkspel')
        break       
    askMove(2)
    win = CheckForWin()
    if win == 2:
        print('geel heeft gewonnen')
        break
    draw = checkForDraw()
    if draw == 1:
        print('Gelijkspel')
        break 
                    
