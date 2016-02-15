# coding=utf8

import curses
from random import randrange,choice
from collections import defaultdict

#游戏操作 

actions = ['Up','Left','Down','Right','Restart','Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions_dict = dict(zip(letter_codes,actions*2))

#主程序 

def main(stdscr):
    
    #初始化
    def init():  
        return 'Game'
    
    def not_game(state):
        pass
    
    
    
