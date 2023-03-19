#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""6
See http://www.codecup.nl/rules_blackhole.php
"""
import random

from Constants import *
from FieldModelView import FieldModelView
from StoneModelView import StoneModelView


class BordModel:
    _fields = []     #[[field in rij0], [fields in rij1] , ...]
    _freeFields = [] # voor snelheidswinst
    _nRows = 0
    
    def __init__(self, nRow=AANTAL_RIJEN):
        self._nRows = nRow
        
        for row in range(nRow) :
           list = []
           for index in range(row + 1) :
               field = FieldModelView(row, index, None, None)
               list.append(field)
               self._freeFields.append(field)
           self._fields.append(list) 
           
        for row in range(nRow) :
           for index in range(row + 1) :
               self._fields[row][index].setNeighbourFields(self._makeNeighbours(row, index))

        self._setOccupiedStones()
          
              
    def _setOccupiedStones(self):
        # Bezet permanent 5 stenen en dus velden op het bord.
        list = []
        for i in range(AANTAL_BLOKKADES):
            while True:
                row = random.randint(0, self._nRows - 1)
                index = random.randint(0, row)
                
                if not((row, index) in list):
                    list.append((row, index))
                    break
                
        for ri in list:
             self._fields[ri[0]][ri[1]].setBlocked() 
             self._fields[ri[0]][ri[1]].setColor(BROWN)
             self._freeFields.remove(self._fields[ri[0]][ri[1]])

     
    def _makeNeighbours(self, row, index) :
        # retourneert een lijst met buurvelden voor field (row, index)
        list = []
        
        # rij boven
        if self._geldigCoord(row - 1, index) and self._fields[row - 1][index]:
            list.append(self._fields[row - 1][index])
        if self._geldigCoord(row - 1, index -1 ):
            list.append(self._fields[row - 1][index - 1])
        # dezelfde rij
        if self._geldigCoord(row, index - 1):
            list.append(self._fields[row][index - 1])
        if self._geldigCoord(row, index + 1):
            list.append(self._fields[row][index + 1])
        #rij onder
        if self._geldigCoord(row + 1, index):
            list.append(self._fields[row + 1][index])
        if self._geldigCoord(row + 1, index + 1):
            list.append(self._fields[row + 1][index + 1])

        return list

       
    def _geldigCoord(self, row, index):
        if row < 0 or row >= self._nRows:
            return False
        
        if index < 0 or index > row:
            return False
        
        return True
    
    def miniMax(self, maximaliseer, color, fields, values, opponentValues, alpha, beta):        
        if len(values) == 0:
            return fields[0].getValueNeighbours() , 0, None
         
        besteVeld = None
        besteSteenWaarde = -1
        besteEindstandWaarde = -100000 if maximaliseer else 100000
        
        for field in fields:
            for waarde in values:
                field.setStone(StoneModelView(color, waarde))
                    
                bw, bsw, bv = self.miniMax(not maximaliseer, 
                                           kleurTegenstander(color), 
                                           list(filter(lambda f: not(f == field), fields)),
                                           opponentValues,
                                           list(filter(lambda x: not(x == waarde), values)),
                                           alpha, beta)           
                field.removeStone()
                
                if maximaliseer: 
                    if bw > beta:
                        return bw, waarde, field 
                        
                    if bw > besteEindstandWaarde:
                        besteEindstandWaarde = bw
                        besteSteenWaarde = waarde
                        besteVeld = field
                        if bw > alpha:
                            alpha = bw
                else:
                    if bw < alpha:
                       return bw, waarde, field 
                   
                    if bw < besteEindstandWaarde:
                        besteEindstandWaarde = bw
                        besteSteenWaarde = waarde
                        besteVeld = field
                        if bw < beta:
                            beta = bw
        
        return besteEindstandWaarde, besteSteenWaarde, besteVeld   
  

    def getFields(self) :
        return self._fields
    
    def getFreeFields(self):
        return self._freeFields
    
    
    def getField(self, xCoord, yCoord):
        for field in self._freeFields:
            if field.inField(xCoord, yCoord) :
                return field
                
        return None
        
      
    def occupyField(self, field):
        # field bevat reeds een stone!
        self._freeFields.remove(field)
 
    
    def releaseStone(self, field):
        # Voegt  indien mogelijk  toe aan _freeFieldsCoord
        field.removeStone()
        if  not ( field in self._freeFields):
            self._freeField.append(f)
              
    
    def print(self):
        spaties = "       "
        row = 0
        for fieldList in self._fields:
            for i in range(self._nRows - row):
                print(spaties, end='')
            for field in fieldList:
                field.print()
                print(" ", end='')
            print("") 
            row = row + 1        


if __name__ == "__main__" :
    bordModel = BordModel()
    bordModel.print()