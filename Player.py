#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from Constants import *


class Player:
    _name = None
    _freeValues = []
    _color = None
    _bordModel = None
    _opponent = None
    
    def __init__(self, bordModel, who, startsGame, opponent):
        self._bordModel = bordModel
        
        self._name = who
        
        if (startsGame):
            self._color = RED
        else:
            self._color=BLUE
            
        self._setFreeValues()
        self._opponent = opponent
    
    
    def _setFreeValues(self):
       self._freeValues = []

       for i in range(1, MAX_VALUE + 1):
           self._freeValues.append(i)
           
    
    def getComputerMove(self):
        # Alhpa-beta algoritme voor de laatste zetten
        if len(self._bordModel.getFreeFields()) <= 6:
            eindWaarde, waardeSteen, veld  =  self._bordModel.miniMax(True, RED, self._bordModel.getFreeFields(), 
                                        self._freeValues, self._opponent.getFreeValues(), -10000, 10000)
            print("eindwaarde : %2d waardeSteen: %2d veld: %15s" %  (eindWaarde, waardeSteen, veld.toString()))
            return veld, waardeSteen
        

        freeFields = self._bordModel.getFreeFields()
        
        #is er een Blackhole die gedicht moet worden?
        for field in freeFields:
            if field.isHole():
                value = field.getValueNeighbours()
                if (self._color == RED and value < 0) or (self._color == BLUE and value > 0) :
                   return field, list(filter(lambda x: x > value, self._freeValues) )[0]  
               
        # veld met de meeste vrije buren
        max = 0
        for field in freeFields:
            tmp = field.getNumberFreeNeighbours()
            if tmp > max:
                max = tmp
                besteField = field

        
        return besteField, self._freeValues[len(self._freeValues) - 1]  
        
       
    def getFreeValues(self):
        return self._freeValues
    
    
    def removeFreeValue(self, value):
        self._freeValues.remove(value)
        
    
    def getColor(self):
        return self._color
