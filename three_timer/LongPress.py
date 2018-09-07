import tkinter as tk
from tkinter import *
import threading 


class LongPressButton(Button):

    def __init__(self,parent,text,bg = 'white',font = '微软雅黑',OnClick = None,LongPress = None):
        super().__init__(parent,text = text,bg = bg,font = font)
        self.pack()
        self.OnClick = OnClick
        self.LongPress = LongPress
        self.setupEvent()
        self.trigger = False
    def setupUI(self):
        pass
    def setupEvent(self):
        self.bind('<Button-1>',self.OnStart)
        self.bind('<ButtonRelease-1>',self.OnRelease)   
    
    
    def LongPressEvent(self):
        if self.LongPress != None:
            self.trigger = True
            self.LongPress()


    def OnStart(self,event):
        self.timer = threading.Timer(1,self.LongPressEvent)
        self.timer.start()


    def OnRelease(self,event):
        if self.OnClick != None:
            if self.trigger == False:
                self.OnClick()
        if self.timer != None:
            self.timer.cancel()
        self.trigger = False
    
