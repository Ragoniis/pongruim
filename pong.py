from tkinter import *
import time
import random

#altura da tela 1920
#height 970
class Menu(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1980x1080')
        self.root.title('Pong.py')
        self.frame = Frame(self.root, bg= 'black')
        self.frame.pack()

        self.canvas = Canvas(self.frame, bg = 'black', height = 1000, width = 1980)
        self.canvas.pack()
        '''
        self.canvas.create_text(600,200,text = 'Pong.py', fill = 'white', font = ('Arial','26','bold'),tag ='lala')
        self.text = self.canvas.create_text(600,400,text = 'Play', fill = 'white', font = ('Arial','24','bold'), tag ='play')
        self.canvas.bind('<1>',self.comeca)
        self.canvas.bind('<Motion>',self.muda)
        '''
        self.start = False

        self.score_player = 0
        self.score_ia = 0
        self.velocidade1 = [10,0]
        self.velocidade2 = [10,8]
        self.velocidade3 = [10,15]
        self.velocidade4 = [10,-8]
        self.velocidade5 = [10,-15]


        self.play = self.canvas.bbox('play')
        self.jogar()
        self.root.mainloop()
    def comeca(self,event):
        if event.x >= self.play[0] and event.x <= self.play[2] and event.y >= self.play[1] and event.y <= self.play[3]:
            self.jogar()


    def muda(self,event):
        if event.x >= self.play[0] and event.x <= self.play[2] and event.y >= self.play[1] and event.y <= self.play[3]:
            self.canvas.itemconfig('play', font = ('italic'))
            return
        self.canvas.itemconfig('play', font = ('Arial','24','bold'))

    def jogar(self):
        self.canvas.delete(ALL)
        time.sleep(0.2)
        self.canvas.create_oval(575,375,625,425, tag = 'ball', fill = 'red')
        self.root.bind('<Key>', self.move_play)
        #ball
        self.canvas.create_oval(575,375,625,425, tag = 'ball', fill = 'white')

        self.text_score_player = self.canvas.create_text(400,100,fill ='white', text = str(self.score_player), font= ('Verdana','60','bold'))
        self.text_score_ia = self.canvas.create_text(1520,100,fill ='white', text = str(self.score_ia), font= ('Verdana','60','bold'))


        #PLAYER
        self.player0 = self.canvas.create_rectangle(205,295,220,320, tag = 'player0', fill ='black')
        self.player1 = self.canvas.create_rectangle(205,320,220,362, fill ='white', tag = 'player1', outline = 'white')
        self.player2 = self.canvas.create_rectangle(205,360,220,440, fill ='white',tag = 'player2', outline = 'white')
        self.player3 = self.canvas.create_rectangle(205,440,220,480, fill ='white', tag = 'player3', outline = 'white')
        self.player4 = self.canvas.create_rectangle(205,480,220,505 ,tag = 'player4', fill ='black')

        #I.A
        self.ia0 = self.canvas.create_rectangle(1700,295,1715,320, fill ='black', tag = 'I.A0')
        self.ia1 = self.canvas.create_rectangle(1700,320,1715,360, fill ='white', tag = 'I.A1', outline = 'white')
        self.ia2 = self.canvas.create_rectangle(1700,360,1715,440, fill ='white', tag ='I.A2', outline = 'white')
        self.ia3 = self.canvas.create_rectangle(1700,440,1715,480, fill ='white', tag ='I.A3', outline = 'white')
        self.ia4 = self.canvas.create_rectangle(1700,480,1715,505, fill ='black', tag ='I.A4')

        self.playing = True
        #velocity of the ball
        self.velocidade = random.choice(([10,0],[10,8],[10,-8],[-10,0],[-10,-8],[-10,-8]))
        if self.start == False :
            self.move_ball()
            self.start = True
    def move_ball(self):
        self. ball = self.canvas.move('ball',self.velocidade[0],self.velocidade[1])
        self.coordb = self.canvas.bbox('ball')
        if self.coordb[1] <= 0 or self.coordb[3]>= 970:
            self.velocidade[1] = -self.velocidade[1]
        colisoes = self.canvas.find_overlapping(*self.coordb)
        if len(colisoes) != 0 :
            acer = self.canvas.find_closest(self.coordb[0],self.coordb[1]+25)
            acer2 = self.canvas.find_closest(self.coordb[2],self.coordb[1]+25)
            if acer[0] == self.player1 or acer[0] == self.player0 :
                self.velocidade = self.velocidade4.copy()
            elif acer[0] == self.player2 :
                self.velocidade[0] = self.velocidade1[0]
                self.ia0 = self.canvas.create_rectangle(1700,295,1715,320, fill ='black', tag = 'I.A0')
                self.velocidade[1] = 0
            elif acer[0] == self.player3 or acer[0] == self.player4:
                self.velocidade = self.velocidade2.copy()
            elif acer2[0] == self.ia1 or acer2[0] == self.ia0 :
                self.velocidade[0] = -self.velocidade[0]
                self.velocidade[1] = self.velocidade4[1]
            elif acer2[0] == self.ia2 :
                self.velocidade[0] = -self.velocidade1[0]
                self.velocidade[1] = 0
            elif acer2[0] == self.ia3 or acer2[0] == self.ia4:
                self.velocidade[1] = self.velocdade2[1]
                self.velocdade[0] = -self.velocidade[0]

        if self.coordb[0] <= 0 :
            self.score_ia += 1
            self.playing == False
            self.jogar()
        elif self.coordb[2] >= 1900 :
            self.score_player += 1
            self.playing == False
            self.jogar()
        self.root.after(1,self.move_ia)
        self.root.after(10,self.move_ball)


    def move_ia(self):
        self.coordia1 = self.canvas.bbox('I.A1')
        self.coordia3 = self.canvas.bbox('I.A3')
        if (self.coordia1[1]+100) >= (self.coordb[1]+25):
            self.canvas.move('I.A0',0,-((self.coordia1[1]+100)-(self.coordb[1]+25))*0.06)
            self.canvas.move('I.A1',0,-((self.coordia1[1]+100)-(self.coordb[1]+25))*0.06)
            self.canvas.move('I.A2',0,-((self.coordia1[1]+100)-(self.coordb[1]+25))*0.06)
            self.canvas.move('I.A3',0,-((self.coordia1[1]+100)-(self.coordb[1]+25))*0.06)
            self.canvas.move('I.A4',0,-((self.coordia1[1]+100)-(self.coordb[1]+25))*0.06)

        elif self.coordia3[3]-100 <= (self.coordb[1]+25):
            self.canvas.move('I.A0',0,-((self.coordia1[3]-100)-(self.coordb[1]+25))*0.06)
            self.canvas.move('I.A1',0,-((self.coordia1[3]-100)-(self.coordb[1]+25))*0.06)
            self.canvas.move('I.A2',0,-((self.coordia1[3]-100)-(self.coordb[1]+25))*0.06)
            self.canvas.move('I.A3',0,-((self.coordia1[3]-100)-(self.coordb[1]+25))*0.06)
            self.canvas.move('I.A4',0,-((self.coordia1[3]-100)-(self.coordb[1]+25))*0.06)

    def move_play(self,event):
        self.coordplayer1 = self.canvas.bbox('player1')
        self.coordplayer3 = self.canvas.bbox('player3')
        if event.char == 'k' and self.playing == True and self.coordplayer1[1] > 0 :
            self.canvas.move('player0', 0 , -30)
            self.canvas.move('player1', 0 , -30)
            self.canvas.move('player2', 0 , -30)
            self.canvas.move('player3', 0 , -30)
            self.canvas.move('player4', 0 , -30)

        elif event.char == 'j' and self.playing == True and self.coordplayer3[3] < 940 :
            self.canvas.move('player0', 0 , 30)
            self.canvas.move('player1', 0 , 30)
            self.canvas.move('player2', 0 , 30)
            self.canvas.move('player3', 0 , 30)
            self.canvas.move('player4', 0 , 30)


Menu()
