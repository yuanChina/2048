# coding=utf8

from random import randrange, choice


#锟斤拷锟斤拷锟斤拷
class GameField(object):
    def __init__(self,height=4,width=4,win=2048):
        self.height = height #锟斤拷锟教高讹拷
        self.width = width #锟斤拷锟教匡拷锟�
        self.win = win #胜锟斤拷锟斤拷锟�
        self.score = 0 #锟斤拷前锟斤拷锟斤拷
        self.heightscore = 0 #锟斤拷叻锟�
        self.reset()   #锟斤拷锟斤拷
        
    #锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷2 4
    def spawn(self):
        new_element = 4 if randrange(100)>89 else 2
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element
        
    def reset(self):
        if self.score > self.heightscore:
            self.heightscore =self.score
            
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()
        
        