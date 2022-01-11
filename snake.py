import turtle
import random as rand
import time

class snake_block(turtle.Turtle):
    '''Serves a 'pixel' that can change color'''

    def __init__(self, x, y, blockLen, initColor):
        turtle.Turtle.__init__(self) # sets up a turtle

        self.up()
        self.hideturtle()
        self.speed()
        self.shapesize(blockLen, blockLen)
        self.color(initColor, initColor)
        self.ogColor = initColor

        self.goto(x, y)
        self.shape('square')
        self.showturtle()

    def revert(self):
        '''Goes back to original color'''

        self.color(self.ogColor, self.ogColor)

class snake_game(turtle.Turtle):
    '''Actual snake game'''

    def __init__(self, numBlock, blockLen):
        '''
        numBlock - Number of blocks wide'''

        turtle.Turtle.__init__(self)
        self.wn = turtle.Screen()
        self.unit = numBlock * blockLen * 20
        self.wn.setup(width = self.unit + 100, height = self.unit + 200)
        self.wn.bgcolor('#223347')

        self.numBlock = numBlock
        self.blockLen = blockLen
        self.blockList = []
        self.headPos = [rand.randrange(0, self.numBlock), rand.randrange(0, self.numBlock)]
        self.bodyPos = [[self.headPos[0], self.headPos[1]]]
        self.snakeLen = 2
        self.vect = [0, 0]
        self.dead = False
        
        self.draw_board()
        self.draw_snake(False, True)

        self.wn.onkeypress(self.game_loop, 'Return')
        self.wn.onkeypress(self.move_up, 'Up')
        self.wn.onkeypress(self.move_right, 'Right')
        self.wn.onkeypress(self.move_down, 'Down')
        self.wn.onkeypress(self.move_left, 'Left')

        self.wn.listen()
        self.wn.mainloop()

    def game_loop(self):
        count = 1
        while not self.dead:
            if count % 2 == 0:
                self.draw_snake(True)
            
            else:
                self.draw_snake()
            
            count += 1
            time.sleep(0.1)

    def draw_snake(self, grow=False, first=False):
        self.wn.tracer(0, 0)

        if grow:
            self.snakeLen += 1

        self.headPos[self.vect[0]] += self.vect[1]
        self.bodyPos.append([self.headPos[0], self.headPos[1]])

        if self.headPos[0] >= self.numBlock or self.headPos[1] >= self.numBlock \
           or self.headPos[0] < 0 or self.headPos[1] < 0:
            self.dead = True

        else:
            self.blockList[self.headPos[0]][self.headPos[1]].color('green', 'green')
            if grow or first:
                pass
                
            elif not grow:
                self.bodyPos.pop(0)

            if not first and not (len(self.bodyPos) == 1):
                self.blockList[self.bodyPos[0][0]][self.bodyPos[0][1]].revert()
            
            elif not first and len(self.bodyPos) == 1:
                self.blockList[self.bodyPos[0][0]][self.bodyPos[0][1]].revert()
        
        self.wn.update()

    def move_up(self):
        if not self.vect == [1, -1]:
            self.vect = [1, 1]

    def move_right(self):
        if not self.vect == [0, -1]:
            self.vect = [0, 1]

    def move_down(self):
        if not self.vect == [1, 1]:
            self.vect = [1, -1]

    def move_left(self):
        if not self.vect == [0, 1]:
            self.vect = [0, -1]

    def draw_board(self):
        '''Draws the snake board
           Stores each block in blockList: (x, y) Q1'''

        self.hideturtle()
        self.wn.tracer(0, 0)

        # border
        self.seth(90)
        self.color('white')
        self.width(5)
        self.goto(-self.unit // 2, -self.unit // 2 - self.blockLen * 20 // 2)
        for i in range(4):
            self.fd(self.unit)
            self.right(90)

        self.up()
        self.seth(90)

        # board
        for i in range(1, self.numBlock + 1):
            self.goto(-self.unit // 2 - (self.blockLen * 20 // 2), -self.unit // 2)
            self.right(90)
            self.fd(self.blockLen * 20 * i)
            self.left(90)

            tempList = []

            for j in range(0, self.numBlock):
                if not j == 0: 
                    self.forward(self.blockLen * 20)
                
                if j % 2 == i % 2:
                    color =  "#2d3f54"
                
                else:
                    color = "#202937"
                
                tempList.append(snake_block(self.xcor(), self.ycor(), self.blockLen, color))
            
            self.blockList.append(tempList)            

        self.wn.update()

game = snake_game(20, 2)
