from big_ol_pile_of_manim_imports import *

class Unity:
    def __init__(self,width,nColumns,nRows,position, cells = [], omitted = False):
        self.width = width
        self.nColumns = nColumns
        self.nRows = nRows
        self.position = position
        self.cells = cells
        self.omitted = omitted
        self.unitySquare = Square(side_length=self.width).move_to(self.position)
        if(self.cells == []):
            self.createCells()
        
    def setWidth(self, newWidth):
        self.width = newWidth

    def setNColumns(self, newNColumns):
        self.nColumns = newNColumns

    def setNRows(self, newNRows):
        self.nRows = newNRows

    def highLightColumns(self, ns, fillColor, opacity = 1):
        for i in range(self.nRows*self.nColumns):
            if i % self.nColumns in ns:
                self.cells[i].set_fill(fillColor,opacity)

    def highLightRows(self, ns, fillColor, opacity = 1):
        for i in range(self.nRows*self.nColumns):
            if i // self.nColumns in ns:
                self.cells[i].set_fill(fillColor,opacity)

    def highLightClear(self):
        for i in range(self.nRows*self.nColumns):
            self.cells[i].set_fill(BLACK,0)

    def highLightCells(self, ns, fillColor, opacity = 1):
        for i in range(self.nRows*self.nColumns):
            if i in ns:
                self.cells[i].set_fill(fillColor,opacity)

    def createCells(self):
        for i in range(self.nRows):
            for j in range(self.nColumns):
                self.cells.append(
                    Rectangle(height=self.width/self.nRows,width=self.width/self.nColumns,fill_opacity=0).move_to(
                        self.unitySquare.get_center()
                        +self.width*(1 - (1+2*(j))/self.nColumns)/2*LEFT
                        +self.width*(1 - (1 + 2*(i))/self.nRows)/2*UP
                    )
                )

    def updateCellsPosition(self):
        for k in range(self.nRows*self.nColumns):
            i = k // self.nColumns
            j = k % self.nColumns
            self.cells[k].move_to(
                        self.unitySquare.get_center()
                        +self.width*(1 - (1+2*(j))/self.nColumns)/2*LEFT
                        +self.width*(1 - (1 + 2*(i))/self.nRows)/2*UP
                    )

    def createVerticalPartitions(self, n):
        self.nColumns *= n
        cellsBeforePartition = self.cells
        m = len(self.cells)
        self.cells = []

        for k in range(m):
            for l in range(n):
                cellsBeforePartition[k].height=self.width/self.nRows
                cellsBeforePartition[k].width=self.width/self.nColumns
                i = k // (self.nColumns // n)
                j = (k*(n) + l) % self.nColumns
                self.cells.append(
                    Rectangle(height=self.width/self.nRows,width=self.width/self.nColumns,fill_opacity=0).move_to(
                        self.unitySquare.get_center()
                        +self.width*(1 - (1+2*(j))/self.nColumns)/2*LEFT
                        +self.width*(1 - (1 + 2*(i))/self.nRows)/2*UP
                    )
                )
                if cellsBeforePartition[k].get_fill_color() != Color("white"):
                    self.cells[-1].set_fill(cellsBeforePartition[k].get_fill_color(),1)
                
    def createHorizontalPartitions(self, n):
        nRowsBeforePartition = self.nRows
        cellsBeforePartition = self.cells
        self.nRows *= n
        self.cells = []

        for k in range(nRowsBeforePartition):
            for l in range(n):
                for m in range(self.nColumns):
                    i = k*n + l
                    j = m % self.nColumns
                    self.cells.append(
                        Rectangle(height=self.width/self.nRows,width=self.width/self.nColumns,fill_opacity=0).move_to(
                            self.unitySquare.get_center()
                            +self.width*(1 - (1+2*(j))/self.nColumns)/2*LEFT
                            +self.width*(1 - (1 + 2*(i))/self.nRows)/2*UP
                        )
                    )
                    if cellsBeforePartition[k*self.nColumns + (m % self.nColumns)].get_fill_color() != Color("white"):
                        self.cells[-1].set_fill(cellsBeforePartition[k*self.nColumns + (m % self.nColumns)].get_fill_color(),1)

    def joinHorizontalPartitions(self, n):
        if self.nRows % n == 0:
            nRowsBeforeJoin = self.nRows
            cellsBeforeJoin = self.cells

            self.nRows = nRowsBeforeJoin // n
            
            nr = self.nRows
            nc = self.nColumns

            #self.nRows = nRowsBeforeJoin // n
            self.cells = []
            
            for r in range(nr):
                for c in range(nc):
                    self.cells.append(
                        Rectangle(
                            height=self.width/self.nRows,
                            width=self.width/self.nColumns,
                            fill_opacity=0
                        ).move_to(
                            self.unitySquare.get_center()
                            +self.width*(1 - (1+2*(c))/self.nColumns)/2*LEFT
                            +self.width*(1 - (1 + 2*(r))/self.nRows)/2*UP
                        )
                    )
                    corCellAtual = cellsBeforeJoin[c + r*n*nc].get_fill_color()
                    if corCellAtual != Color("white"):
                        self.cells[-1].set_fill(corCellAtual,1)
            print(len(self.cells))
    
    def joinVerticalPartitions(self, n):
        if self.nColumns % n == 0:
            nColumnsBeforeJoin = self.nColumns
            cellsBeforeJoin = self.cells

            self.nColumns = nColumnsBeforeJoin // n
            
            nr = self.nRows
            nc = self.nColumns

            self.cells = []

            for r in range(nr):
                for c in range(nc):
                    self.cells.append(
                        Rectangle(
                            height=self.width/self.nRows,
                            width=self.width/self.nColumns,
                            fill_opacity=0
                        ).move_to(
                            self.unitySquare.get_center()
                            +self.width*(1 - (1+2*(c))/self.nColumns)/2*LEFT
                            +self.width*(1 - (1 + 2*(r))/self.nRows)/2*UP
                        )
                    )
                    corCellAtual = cellsBeforeJoin[r*nColumnsBeforeJoin + c*n].get_fill_color()
                    if corCellAtual != Color("white"):
                        self.cells[-1].set_fill(corCellAtual,1)

    def rotate(self, refUnity, rotationMode = 1):  
        c1 = refUnity.cells
        c2 = []
        nc1 = refUnity.nColumns
        nr1 = refUnity.nRows

        if rotationMode % 2 == 0:
            self.nColumns = nc1
            self.nRows = nr1
        else:
            self.nColumns = nr1
            self.nRows = nc1

        self.cells = []
        
        #Maluquice: (que funciona!)
        for nRotacao in range(rotationMode):
            c2 = []
            for k in range(nc1*nr1):
                c2.append(c1[ (nc1 - 1 + k*nc1) % (nc1*nr1 + 1) ])
            c1 = c2
            p = nc1
            nc1 = nr1
            nr1 = p

        self.cells = c2