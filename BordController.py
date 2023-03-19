#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from Constants import *
from BordModel import BordModel
from BordView import BordView
from StoneModelView import StoneModelView
from Player import Player


class BordController:
    _bordModel = None
    _bordView = None
    _computerPlayer = None
    _humanPlayer = None

    
    def __init__(self, root, computerStarts=True, nRow=AANTAL_RIJEN):
        self._bordModel = BordModel()
        self._bordView = BordView(root, self._bordModel, self)
           
        self._humanPlayer = Player(self._bordModel, HUMAN, not computerStarts, None)
        self._computerPlayer = Player(self._bordModel, COMPUTER, computerStarts, self._humanPlayer)
     
        
    def plaatsPlayerStone(self, event, value):
        field = self._bordModel.getField(event.x, event.y)
        
        if not (field == None):
            field.setStone(StoneModelView(BLUE, value))
            self._bordModel.occupyField(field)
            self._bordView.drawField(field)
            self._humanPlayer.removeFreeValue(value)
            self._bordView.removeCurrentValue()
            
            field, value = self._computerPlayer.getComputerMove()
            self.plaatsComputerStone(field, value)
   
         
    def plaatsComputerStone(self, field, value):
        if not (field == None):
            field.setStone(StoneModelView(RED, value))
            self._bordModel.occupyField(field)
            self._bordView.drawField(field)
            self._computerPlayer.removeFreeValue(value)
   
         
def main():
    root = Tk()
    BordController(root)
    root.mainloop()  


if __name__ == "__main__" :
    main()
