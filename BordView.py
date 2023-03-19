from tkinter import *
from tkinter.font import Font
from Constants import *
from BordModel import BordModel
from math import sqrt


class BordView():
    bordModel = None
    bordController = None
    _nRows = 0
    canvas = None
    waardenLijst=None
    root = None

  
    def __init__(self, root, bordModel, bordController):
        super().__init__()
        self.root = root
        self.bordModel = bordModel
        self.bordController = bordController
        self.initUI(root)


    def initUI(self, root):
        root.title("Blackhole")
        frame = Frame(root)
        frame.pack(fill=BOTH, expand=True)
        
        self.maakP1(frame)
        self.setBindings()
        root.geometry("880x720+10+20")
        self.drawGameBoard(1, 1, 80)


    def maakP1(self, frame):
        p1 = PanedWindow(frame, orient=VERTICAL)
        p1.pack(fill=BOTH, expand=True, padx=20)

        top = Label(p1, text=" ")
        top.pack()
        p1.add(top)
        
        self.maakP2(p1)


    def maakP2(self, p1):    
        p2 = PanedWindow(p1, orient=HORIZONTAL)
        p2.pack(fill=BOTH, expand=True)
        p1.add(p2)

        self.maakP3(p2)

        self.canvas = Canvas(p2) 
        p2.add(self.canvas)


    def maakP3(self, p2):
        p3 = PanedWindow(p2, orient=VERTICAL)
        p3.pack(fill=BOTH, expand=True)
        p2.add(p3)

        waardeLab =  Label(p3, text="Kies een waarde", 
                           font=Font(family='helvetica', size=14, weight='bold'))
        waardeLab.pack()
        p3.add(waardeLab)
        
        self.maakP4(p3)

        p3.add(Label(p3, text=""))


    def maakP4(self, p3):
        p4 = PanedWindow(p3, orient=HORIZONTAL)
        p4.pack(fill=BOTH, expand=True)
        p3.add(p4)
        self.waardenLijst = Listbox(p4, width=5)
        p4.add(self.waardenLijst)

        for i in range(1, MAX_VALUE + 1):
            self.waardenLijst.insert(END, i)

        self.waardenLijst.selection_set(0)
        scrollbar = Scrollbar(p4, width=5)

        p4.add(scrollbar)
        
        dummyLab =  Label(p4, text="  ")
        dummyLab.pack()
        p4.add(dummyLab)

        # attach listbox to scrollbar
        self.waardenLijst.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.waardenLijst.yview)
        
        
    def removeCurrentValue(self):
        self.waardenLijst.delete(self.waardenLijst.curselection())
        if (self.waardenLijst.size() >= 0):
            self.waardenLijst.selection_set(0)


    def drawGameBoard(self, linksbovenX, linksbovenY, breedteHexagon):
        aantal = AANTAL_RIJEN
        stapY = 0.5 * breedteHexagon * sqrt(3)

        fields = self.bordModel.getFields();
        for i in range(0, aantal):
            for j in range(0, i + 1):
                fields[i][j].draw(self.canvas, 
                      linksbovenX + (aantal - 1 + 2 * j - i) * breedteHexagon/2 + 2,
                      linksbovenY + i * stapY, breedteHexagon)
                
                
    def plaatsPlayerStone(self, event):
        index = self.waardenLijst.curselection()
        if len(index) > 0 :
            self.bordController.plaatsPlayerStone(event, self.waardenLijst.get(index))
 
              
    def drawField(self, field):
        field.draw(self.canvas)


    def setBindings(self):
        self.canvas.bind("<Button-1>", self.plaatsPlayerStone) 
        

         
       
