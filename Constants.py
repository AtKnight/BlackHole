#!/usr/bin/env python3
# -*- coding: utf-8 -*-


COMPUTER='Computer'
HUMAN='Mens'

#Color names for tkinter
RED = 'red'
BLUE = 'blue'
BLOCKED = BROWN = 'saddle brown'
EMPTY = GREY = 'snow2'
BLACK = 'black'

COLOR_SHORT = {RED:"R", BLUE:"B", BROWN:"X", GREY:"G", BLACK:"Z"}

# board
AANTAL_RIJEN = 8
AANTAL_BLOKKADES = 5 # aantal bruine stenen

# De stenen hebben de waarde 1, 2, 3, MAX_VALUE
MAX_VALUE = round(((AANTAL_RIJEN + 1) * AANTAL_RIJEN / 2 - AANTAL_BLOKKADES - 1) / 2)


def kleurTegenstander(color):
    return RED if color == BLUE else  BLUE