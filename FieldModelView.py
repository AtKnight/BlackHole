#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from Constants import *
from tkinter import Canvas, BOTH
from functools import *
from math import sqrt

class FieldModelView:
    _backgroundColor = None
    _linksbovenX = 0
    _linksbovenY = 0
    _breedte = 0
    centerX = 0
    centerY = 0
    row = 0
    index = 0
    stone = None
    neighbourFields = None
    _blocked = False
    
    
    def __init__(self, row, index, stone, neighbourFields, backgroundColor=GREY) :
        self.row = row
        self.index = index
        self.stone = stone
        self.neighbourFields = neighbourFields
        self._backgroundColor=backgroundColor
        self._blocked = False
  
      
    def getStoneColor(self):
        return self.stone.color
    
    def setColor(self, color):
        self._backgroundColor = color
        
    def setStone(self, stone):
        self.stone = stone
        self._blocked = True
        
    def removeStone(self):
        self.stone = None
        self._blocked = False
        
    def setNeighbourFields(self, nbf):
        self.neighbourFields = nbf
       
    def getNeighboursFields(self) :
        return self.neighboursFields
    
    def getNumberFreeNeighbours(self):
        return len(list(filter(lambda f: not f.isOccupied(), self.neighbourFields)))
    
    def setBlocked(self):
        self._blocked = True
        
    def isOccupied(self):
        return self._blocked 
 
    def isHole(self):
        #Dit veld is leeg en de aangrenzende buurvelden zijn gevuld
        if self.isOccupied():
            return False
            
        return reduce(lambda x, y: x and y, map(lambda f: f.isOccupied(), self.neighbourFields))
 
    
    def getStoneValue(self):
        if self.stone == None:
            return 0
        
        return self.stone.getValue()
 
    
    def getValueNeighbours(self):
        return reduce(lambda x, y: x + y, map(lambda x: x.getStoneValue(), self.neighbourFields))
    
    
    def inField(self, x, y):
        d = (self.centerX - x) * (self.centerX - x) + (self.centerY - y) * (self.centerY - y)
        kw= self._breedte * self._breedte / 4 

        return (d < kw) and ( not self._blocked)
            
    
    def toString(self):
        if self.stone == None:
            inhoud = "LEEG"
        else :
            inhoud = self.stone.toString()
            
        return "{(%d,%d) %s}" % (self.row, self.index, inhoud)
 
    
    def print(self):
        print(self.toString(), end='')
        
    ############################
    # View methods
    ############################
    
    def draw(self, canvas, linksbovenX = None, linksbovenY = None, breedte = None):
        if linksbovenX == None:
             linksbovenX = self._linksbovenX
             linksbovenY = self._linksbovenY
             breedte = self._breedte
        else :
            self._linksbovenX = linksbovenX
            self._linksbovenY = linksbovenY
            self._breedte = breedte
            self.can = canvas
        
        x0 = self._linksbovenX
        y0 = self._linksbovenY
        
        stepX = 0.5 * breedte
        stepY = 0.5 * breedte / sqrt(3)
        lengteRibbe = breedte /sqrt(3)
        
        x1 = x4 = x0 + stepX
        x2 = x3 = x0 + breedte
        x5 = x6 = x0
        
        y1 = y0 
        y6 = y2 = y0 + stepY
        y5 = y3 = y2 + lengteRibbe
        y4 = y3 + stepY
         
        points = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6]
        canvas.create_polygon(points, outline=BLACK, fill=self._backgroundColor, width=2)

        
        self.drawStone(canvas, linksbovenX, 
                       linksbovenY + stepY + 0.5 * lengteRibbe - 0.5 * breedte, breedte)
        
        self.centerX = (x2 + x6) / 2
        self.centerY = (y1 + y4) / 2
 
       
    def drawStone(self, canvas, linksbovenX, linksbovenY, breedte):
        if self.stone != None:
            self.stone.draw(canvas, linksbovenX, linksbovenY, breedte)
     
      
