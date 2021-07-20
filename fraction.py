#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *
from unity import *

class Teste(Scene):
    def construct(self):
        #self.somaAlgebrica("-2/3","4/5") 
        #self.somaAlgebrica("-4/5","1/2") 
        #self.somaAlgebrica("-1/2","4/5") 
        #self.somaAlgebrica("1/2","-4/5")  
        #self.somaAlgebrica("2/5","1/2") 
        #self.somaAlgebrica("2/6","-6/6")
        
        #self.multiplicar("-2/5","-2/4")
        #self.multiplicar("2/5","2/4") 
        #self.multiplicar("-3/5","2/4") 
        #self.multiplicar("1/5","3/4") 
        #self.multiplicar("-1/5","-2/4") 
        #self.multiplicar("4/5","-1/4") 
        
        #self.dividir("1/4","1/3")
        #self.dividir("-1/4","1/3")
        self.dividir("1/4","-1/3")
        #self.dividir("-1/4","-1/3")
        #self.sample1()
        
    def sample1(self):
        
        UNITY_WIDTH = 2
        position1 = 3*LEFT 
        position2 = 0*RIGHT
        position3 = 3*RIGHT
        positionEquals = 1.5*RIGHT
        positionTimes = 1.5*LEFT 

        u1 = Unity(width=UNITY_WIDTH, nColumns = 3, nRows = 2, position = position1, cells=[])
        u2 = Unity(width=UNITY_WIDTH, nColumns = 2, nRows = 2, position = position2, cells=[])
        u3 = Unity(width=UNITY_WIDTH, nColumns = 3, nRows = 2, position = position1, cells=[])

        plus = TexMobject(r"\times").move_to(positionTimes)
        equals = TexMobject(r"=").move_to(positionEquals)

        self.play(
            Write(plus),
            Write(equals)
        )
        
        h1 = [0,2,4]
        h2 = [0]

        c1 = BLUE
        c2 = RED

        u1.highLightCells(h1, c1)
        u2.highLightCells([0], c2)
        u3.highLightCells(h1, c1)

        self.plotUnity(u1)
        self.plotUnity(u2)
        self.plotUnity(u3)

        self.moveUnity(u3,position3)

        coloredCells = []
        nonColoredCells = []
        colorsForNewParts = []
        for i in range(len(u3.cells)):
            nonColoredCells.append(i)
        coloredCells = u3.getCellsByColor([BLUE,RED])
        nonColoredCells = list(set(nonColoredCells) - set(coloredCells))

        #self.multiplyUnits(u2, u3, coloredCells, "TransformFromCopy")
        
        self.multiplyUnits(u2, u3, coloredCells, "TRANSFORMFROMCOPYPAUSING")

        self.wait()

        self.multiplyUnits(u2, u3, nonColoredCells, "FadeIn", BLACK)

    def dividir(self, n1, n2):
        # transforma a string recebida em 4 variáveis:
        # Numerador e Denominador de cada fração.

        info = (n1+"/"+n2).split("/")
        a = int(info[0])
        b = int(info[1])
        c = int(info[2])
        d = int(info[3])
        
        division = (a/b) / (c/d)

        if abs(division) > 1:
            raise Exception("Ainda não é possível efetuar divisões cujo resultado é maior que 1.\nSua divisão deu "+str(division))

        if a<0:
            cor1=RED
        else:
            cor1=BLUE

        if c<0:
            cor2=RED
        else:
            cor2=BLUE

        if cor2 == cor1:
            cor3 = BLUE
        else:
            cor3 = RED

        titulo = TexMobject(
            r"\text{Vamos resolver }{"+str(a)+r"\phantom{}"+r"\over"+str(b)+r"} : {"+str(c)+r"\phantom{}"+r"\over"+str(d)+r"}",
            tex_to_color_map={"{"+str(a)+r"\phantom{}": cor1,"{"+str(c)+r"\phantom{}": cor2}
        ).to_corner(UP)
        
        self.play(Write(
            titulo
        ))

        # Criar unidades (Denominadores)

        UNITY_WIDTH = 2
        position1 = 3*LEFT 
        position2 = 0*RIGHT
        position3 = 3*RIGHT
        positionEquals = 1.5*RIGHT
        positionDiv = 1.5*LEFT 

        u1 = Unity(width=UNITY_WIDTH, nColumns = b, nRows = 1, position = position1, cells=[])
        u2 = Unity(width=UNITY_WIDTH, nColumns = 1, nRows = d, position = position2, cells=[])
        u3 = Unity(width=UNITY_WIDTH, nColumns = b, nRows = d, position = position3, cells=[])

        # Pintar os numeradores de acordo com as frações recebidas

        h1 = [] 
        h2 = []
        
        for i in range(abs(a)): 
            h1.append(i)
        for i in range(abs(c)): 
            h2.append(abs(c)-i-1)

        u1.highLightCells(h1, cor1)
        u2.highLightCells(h2, cor2)

        # Mostrar a Unidade 1

        self.plotUnity(u1)
        
        # Criar e mostrar o sinal de divisão

        plus = TexMobject(r":").move_to(positionDiv)
        
        self.play(Write(
            plus
        ))
        
        # Mostrar a Unidade 2

        self.plotUnity(u2)
        
        # Criar e mostrar o sinal de igual

        equals = TexMobject(r"=").move_to(positionEquals)

        self.play(Write(
            equals
        ))

        # Particionar

        u1 = self.partitionate(u1,"HORIZONTAL",d)

        u2 = self.partitionate(u2,"VERTICAL",b)

        o1 = u1.getCellsByColor([BLUE,RED])
        o2 = u2.getCellsByColor([BLUE,RED])

        t1=[]
        t2=[]

        for i in range(len(o2)):
            t2.append(i)
        for i in range(len(o1)):
            t1.append(i)

        #self.transferDestroyCells(u2,u3,o2,t2)
        self.play(
            *[
                TransformFromCopy(u2.cells[k],u3.cells[k])
                for k in range(len(t2))
            ],
            *[
                Transform(u2.cells[k],u2.cells[k].set_fill(u2.cells[k].get_fill_color(),opacity=0.3))
                for k in range(len(t2))
            ]
        )

        self.transferDestroyCells(u1,u3,o1,t1,cor1,0.3,cor3)

        u2.highLightCells(o2,cor2)
        u1.highLightCells(o1,cor1)
        
        self.wait()

    def multiplicar(self,n1,n2):
        # transforma a string recebida em 4 variáveis:
        # Numerador e Denominador de cada fração.

        info = (n1+"/"+n2).split("/")
        a = int(info[0])
        b = int(info[1])
        c = int(info[2])
        d = int(info[3])
        
        prod = (a/b) * (c/d)

        if abs(prod) > 1:
            raise Exception("Ainda não é possível efetuar multiplicações cujo resultado é maior que 1.\nSeu produto deu "+str(prod))

        if a<0:
            cor1=RED
        else:
            cor1=BLUE

        if c<0:
            cor2=RED
        else:
            cor2=BLUE

        if cor2 == cor1:
            cor3 = BLUE
        else:
            cor3 = RED

        titulo = TexMobject(
            r"\text{Vamos resolver }{"+str(a)+r"\phantom{}"+r"\over"+str(b)+r"} \times {"+str(c)+r"\phantom{}"+r"\over"+str(d)+r"}",
            tex_to_color_map={"{"+str(a)+r"\phantom{}": cor1,"{"+str(c)+r"\phantom{}": cor2}
        ).to_corner(UP)
        
        self.play(Write(
            titulo
        ))

        # Criar unidades (Denominadores)

        UNITY_WIDTH = 2
        position1 = 3*LEFT 
        position2 = 0*RIGHT
        position3 = 3*RIGHT
        positionEquals = 1.5*RIGHT
        positionTimes = 1.5*LEFT 

        u1 = Unity(width=UNITY_WIDTH, nColumns = b, nRows = 1, position = position1, cells=[])
        u2 = Unity(width=UNITY_WIDTH, nColumns = 1, nRows = d, position = position2, cells=[])
        u3 = Unity(width=UNITY_WIDTH, nColumns = b, nRows = 1, position = position1, cells=[])

        # Pintar os numeradores de acordo com as frações recebidas

        h1 = [] 
        h2 = []
        
        for i in range(abs(a)): 
            h1.append(i)
        for i in range(abs(c)): 
            h2.append(abs(c)-i-1)

        print(h2)

        u1.highLightCells(h1, cor1)
        u2.highLightCells(h2, cor2)
        u3.highLightCells(h1, cor1)

        # Mostrar a Unidade 1

        self.plotUnity(u1)
        
        # Criar e mostrar o sinal de soma

        plus = TexMobject(r"\times").move_to(positionTimes)
        
        self.play(Write(
            plus
        ))
        
        # Mostrar a Unidade 2

        self.plotUnity(u2)
        
        # Criar e mostrar o sinal de igual

        equals = TexMobject(r"=").move_to(positionEquals)

        self.play(Write(
            equals
        ))

        # Copiar unidade 1 para o resultado

        self.plotUnity(u3)

        self.moveUnity(u3,position3)
        
        # Deformar Unidade 2 para células coloridas da Unidade 1 
        # Encontrar células coloridas da u3
        coloredCells = []
        nonColoredCells = []
        colorsForNewParts = []
        
        for i in range(len(u3.cells)):
            nonColoredCells.append(i)

        # Descobrir celulas coloridas e não coloridas
        coloredCells = u3.getCellsByColor([BLUE,RED])
        nonColoredCells = list(set(nonColoredCells) - set(coloredCells))
        
        
        print(coloredCells)
        print(nonColoredCells) 

        #self.multiplyUnits(u2, u3, coloredCells, "TransformFromCopy")
        
        self.multiplyUnits(u2, u3, coloredCells, "TRANSFORMFROMCOPYPAUSING")

        self.wait()

        self.multiplyUnits(u2, u3, nonColoredCells, "FadeIn", BLACK)

    def somaAlgebrica(self,n1,n2,simplifySignal = True):
        # transforma a string recebida em 4 variáveis:
        # Numerador e Denominador de cada fração.

        info = (n1+"/"+n2).split("/")
        a = int(info[0])
        b = int(info[1])
        c = int(info[2])
        d = int(info[3])
        
        soma = a/b + c/d
        
        print(info)
        print(soma)
        print(a)
        print(b)
        print(c)
        print(d)

        if abs(soma) > 1:
            raise Exception("Ainda não é possível efetuar somas cujo resultado é maior que 1.\nSua soma deu "+str(soma))

        if a<0:
            cor1=RED
        else:
            cor1=BLUE

        if c<0:
            cor2=RED
        else:
            cor2=BLUE

        titulo = TexMobject(
            r"\text{Vamos resolver }{"+str(a)+r"\phantom{}"+r"\over"+str(b)+r"} + {"+str(c)+r"\phantom{}"+r"\over"+str(d)+r"}",
            tex_to_color_map={"{"+str(a)+r"\phantom{}": cor1,"{"+str(c)+r"\phantom{}": cor2}
        ).to_corner(UP)
        
        self.play(Write(
            titulo
        ))

        # Criar unidades (Denominadores)

        UNITY_WIDTH = 2
        position1 = 3*LEFT 
        position2 = 0*RIGHT
        position3 = 3*RIGHT
        positionEquals = 1.5*RIGHT
        positionPlus = 1.5*LEFT 

        u1 = Unity(width=UNITY_WIDTH, nColumns = b, nRows = 1, position = position1, cells=[])
        u2 = Unity(width=UNITY_WIDTH, nColumns = 1, nRows = d, position = position2, cells=[])
        u3 = Unity(width=UNITY_WIDTH, nColumns = b, nRows = d, position = position3, cells=[])

        # Pintar de azul os numeradores

        h1 = [] 
        h2 = []
        
        for i in range(abs(a)): 
            h1.append(i)
        for i in range(abs(c)): 
            h2.append(abs(c)-i-1)

        u1.highLightCells(h1, cor1)
        u2.highLightCells(h2, cor2)
        
        # Mostrar a Unidade 1

        self.plotUnity(u1)
        
        # Criar e mostrar o sinal de soma

        plus = TexMobject(r"+").move_to(positionPlus)
        
        self.play(Write(
            plus
        ))
        
        # Mostrar a Unidade 2

        self.plotUnity(u2)
        
        # Criar e mostrar o sinal de igual

        equals = TexMobject(r"=").move_to(positionEquals)

        self.play(Write(
            equals
        ))

        # Particionar

        u1 = self.partitionate(u1,"HORIZONTAL",d)

        u2 = self.partitionate(u2,"VERTICAL",b)

        self.plotUnity(u3)

        # Extrair origem das células que comporão a soma

        o1=[] 
        o2=[]

        for i in range(u1.nColumns*u1.nRows):
            if h1.count(i%u1.nColumns) > 0:
                o1.append(i)
            if h2.count(i//u2.nColumns) > 0:
                o2.append(i)

        # Criar o alvo das células

        t1=[]
        t2=[]

        m = min(len(o1),len(o2))
        d = abs(len(o1)-len(o2))
        for i in range(len(o1)): 
            t1.append(i)
        for i in range(len(o2)): 
            if cor2 == cor1:
                t2.append(len(o1)+i)
            else:
                t2.append(i)


        # Transferir células para a Unity do resultado
        
        self.transferCells(u1,u3,o1,t1,cor1)
        if cor1 == cor2:
            self.transferCells(u2,u3,o2,t2,cor2)
        else:
            # Separar a transferência das células em duas partes:
            # A parte que irá "zerar" a fração primeiro
            eliminationOrigin = o2[:m]
            eliminationTarget = t2[:m] 
            # A parte que irá completar o resultado |u1| > |u2|
            thereIsARemainder = abs(a/b) > abs(c/d)
            if thereIsARemainder:
                remainderOrigin = o2[-d:]
                remainderTarget = t2[-d:]

            # Zerar fração
            self.transferDestroyCells(u2,u3,eliminationOrigin,eliminationTarget,cor2)

            # Calcular último resultado
            if thereIsARemainder:
                self.transferCells(u2,u3,remainderOrigin,remainderTarget,cor2)

        self.wait()

        u1.highLightCells(o1, cor1)
        u2.highLightCells(o2, cor2)

        self.wait()

    # Método obsoleto (pela somaAlgebrica)
    def somar(self,n1,n2):
        # transforma a string recebida em 4 variáveis:
        # Numerador e Denominador de cada fração.

        info = (n1+"/"+n2).split("/")
        a = int(info[0])
        b = int(info[1])
        c = int(info[2])
        d = int(info[3])
        
        soma = a/b + c/d

        if abs(soma) > 1:
            raise Exception("Ainda não é possível efetuar somas cujo resultado é maior que 1.\nSua soma deu "+str(soma))



        titulo = TexMobject(
            r"\text{Vamos resolver }{"+str(a)+r"\phantom{}"+r"\over"+str(b)+r"} + {"+str(c)+r"\phantom{}"+r"\over"+str(d)+r"}",
            tex_to_color_map={"{"+str(a)+r"\phantom{}": BLUE,"{"+str(c)+r"\phantom{}": BLUE}
        ).to_corner(UP)
        
        self.play(Write(
            titulo
        ))

        # Criar unidades (Denominadores)

        UNITY_WIDTH = 2
        position1 = 3*LEFT 
        position2 = 0*RIGHT
        position3 = 3*RIGHT
        positionEquals = 1.5*RIGHT
        positionPlus = 1.5*LEFT 

        u1 = Unity(width=UNITY_WIDTH, nColumns = b, nRows = 1, position = position1, cells=[])
        u2 = Unity(width=UNITY_WIDTH, nColumns = 1, nRows = d, position = position2, cells=[])
        u3 = Unity(width=UNITY_WIDTH, nColumns = b, nRows = d, position = position3, cells=[])

        # Pintar de azul os numeradores

        h1 = [] 
        h2 = []
        
        for i in range(a): 
            h1.append(i)
        for i in range(c): 
            h2.append(c-i)

        u1.highLightCells(h1, BLUE)
        u2.highLightCells(h2, BLUE)
        
        # Mostrar a Unidade 1

        self.plotUnity(u1)
        
        # Criar e mostrar o sinal de soma

        plus = TexMobject(r"+").move_to(positionPlus)
        
        self.play(Write(
            plus
        ))
        
        # Mostrar a Unidade 2

        self.plotUnity(u2)
        
        # Criar e mostrar o sinal de igual

        equals = TexMobject(r"=").move_to(positionEquals)

        self.play(Write(
            equals
        ))

        # Particionar

        u1 = self.partitionate(u1,"HORIZONTAL",d)

        u2 = self.partitionate(u2,"VERTICAL",b)

        self.plotUnity(u3)

        # Extrair origem das células que comporão a soma

        o1=[] 
        o2=[]

        for i in range(u1.nColumns*u1.nRows):
            if h1.count(i%u1.nColumns) > 0:
                o1.append(i)
            if h2.count(i//u2.nColumns) > 0:
                o2.append(i)

        # Criar o alvo das células

        t1=[]
        t2=[]
        for i in range(len(o1)): 
            t1.append(i)
        for i in range(len(o2)): 
            t2.append(len(o1)+i)

        # Transferir células para a Unity do resultado
        
        self.transferCells(u1,u3,o1,t1)
        self.transferCells(u2,u3,o2,t2)

        self.wait()

        u1.highLightCells(o1, BLUE)
        u2.highLightCells(o2, BLUE)

        self.wait()

    def plotUnity(self, unity):
        self.add(
            unity.unitySquare,
            *[
            unity.cells[i]
            for i in range(unity.nColumns*unity.nRows)
            ]
        )

    def showUnity(self, unity, timer=0.35,firsttime=False):
        if not firsttime:
            self.play(
                FadeIn(unity.unitySquare)
            )
            self.wait(timer)
            self.play(
                *[
                FadeIn(unity.cells[i])
                for i in range(unity.nColumns*unity.nRows)
                ]
            )
        else:
            self.play(
                ShowCreation(unity.unitySquare)
            )
            self.wait(timer)
            self.play(
                *[
                ShowCreation(unity.cells[i])
                for i in range(unity.nColumns*unity.nRows)
                ]
            )

    def plotUnity(self, unity):
        self.play(
            FadeIn(unity.unitySquare),
            *[
            FadeIn(unity.cells[i])
            for i in range(unity.nColumns*unity.nRows)
            ]
        )

    def partitionate(self,unity, partition, nParts, timer=0.35):
        unity2 = Unity(width=unity.width, nColumns = unity.nColumns, nRows = unity.nRows, position = unity.position, cells = unity.cells)
        if partition == 'VERTICAL':
            unity2.createVerticalPartitions(nParts)
        elif partition == 'HORIZONTAL':
            unity2.createHorizontalPartitions(nParts)
        else:
            return unity

        self.showUnity(unity2)
        self.wait(timer)
        self.removeUnity(unity) 
        return unity2

    def joinPartitions(self, unity, partition, nParts, timer=0.35):
        unity2 = Unity(width=unity.width, nColumns = unity.nColumns, nRows = unity.nRows, position = unity.position, cells = unity.cells)
        if partition == 'VERTICAL':
            unity2.joinVerticalPartitions(nParts)
        elif partition == 'HORIZONTAL':
            unity2.joinHorizontalPartitions(nParts)
        else:
            return unity
       

        self.wait(timer)

        self.add(
            unity2.unitySquare,
            *[
            unity2.cells[i]
            for i in range(unity2.nColumns*unity2.nRows)
            ]
        )
        
        self.remove(
            unity.unitySquare,
            *[
            unity.cells[i]
            for i in range(unity.nColumns*unity.nRows)
            ]
        )

        return unity2

    def moveUnity(self,unity, position):
        unity.position = position
        self.play(
            ApplyMethod(unity.unitySquare.move_to, position),
            *[
            ApplyMethod(unity.cells[i].move_to, position+unity.width*(1 - (1+2*(i % unity.nColumns))/unity.nColumns)/2*LEFT
                        +unity.width*(1 - (1 + 2*(i // unity.nColumns))/unity.nRows)/2*UP)
            for i in range(unity.nColumns*unity.nRows)
            ]
        )

    def shiftUnity(self,unity, position):
        unity.position = unity.position + position
        self.play(
            ApplyMethod(unity.unitySquare.shift, position),
            *[
            ApplyMethod(unity.cells[i].shift, position)
            for i in range(unity.nColumns*unity.nRows)
            ]
        )

    def fadeUnityCells(self,unity):
        newCells=[]
        for i in range(unity.nColumns*unity.nRows):
            newCells.append(unity.cells[i].set_fill(BLACK,0))
        self.play(
            *[
            Transform(unity.cells[i],newCells[i])
            for i in range(unity.nColumns*unity.nRows)
            ]
        )

    def removeUnity(self,unity, timer=0.35):
        if not unity.omitted:
            self.play(
                *[
                FadeOut(unity.cells[i])
                for i in range(unity.nColumns*unity.nRows)
                ]
            )
            self.wait(timer)
            self.play(
                Uncreate(unity.unitySquare)
            )
        else:
            notOmittedCellsIds = []
            for i in range(unity.nColumns*unity.nRows):
                if unity.cells[i].get_fill_color() not in [None,Color("white")]:
                    notOmittedCellsIds.append(i)
            self.play(
                *[
                FadeOut(unity.cells[i])
                for i in notOmittedCellsIds
                ]
            )
    
    def rotateUnity(self, unity, angle, timer = 0.35):
        if angle % 90 == 0:
            rotationMode = (angle % 360) // 90
            unity.rotate(unity, rotationMode)

            self.play(
                Rotate(
                    unity.unitySquare,
                    angle*DEGREES,
                    about_point=unity.unitySquare.get_center()
                ),
                *[
                Rotate(
                    unity.cells[i],
                    angle*DEGREES,about_point=unity.unitySquare.get_center()
                )
                for i in range(unity.nColumns*unity.nRows)
                ]
            )

            self.wait(timer)      

    def toggleUnityGrid(self, unity):
        unity.omitted = not unity.omitted
        cellsToToggleGrid = []

        for i in range(unity.nColumns*unity.nRows):
            if unity.cells[i].get_fill_color() in [None,Color("white")]:
                cellsToToggleGrid.append(i)

        if unity.omitted:
            self.play(
                FadeOut(unity.unitySquare),
                *[
                FadeOut(unity.cells[i])
                for i in cellsToToggleGrid
                ]
            )
        else:
            self.play(
                FadeIn(unity.unitySquare),
                *[
                FadeIn(unity.cells[i])
                for i in cellsToToggleGrid
                ]
            )
    
    def switchCellsPosition(self, unity, x1, x2):
        C1 = unity.cells[x1]
        C2 = unity.cells[x2]
        pos1 = C1.get_center()
        pos2 = C2.get_center()
        unity.cells[x1] = C2
        unity.cells[x2] = C1
        self.play(
            ApplyMethod(unity.cells[x1].move_to, pos1),
            ApplyMethod(unity.cells[x2].move_to, pos2)
        )

    def normalizeUnity(self, unity, mode = "UL", animate = True):
        targets = []
        nc = unity.nColumns
        nr = unity.nRows
        currentTarget = 0

        up_to_down = range(nr)
        down_to_up = range(nr-1,-1,-1)
        left_to_right = range(nc)
        right_to_left = range(nc-1,-1,-1)
        
        rangeI = None
        rangeJ = None

        if mode in ["UL","UR","DL","DR"]:
            # x = i*nc + j

            if mode == "UL":
                rangeI = up_to_down
                rangeJ = left_to_right
            elif mode == "UR":
                rangeI = up_to_down
                rangeJ = right_to_left
            elif mode == "DL":
                rangeI = down_to_up
                rangeJ = left_to_right
            else: 
                rangeI = down_to_up
                rangeJ = right_to_left
            for i in rangeI:
                for j in rangeJ:
                    l = len(targets)
                    x = i*nc + j
                    c = unity.cells[x].get_fill_color()
                    if c in [Color("white"),None]:
                        targets.append(x)
                    else:
                        if not l == 0:
                            self.switchCellsPosition(unity,x,targets[currentTarget])
                            targets.append(x)
                            currentTarget += 1 

        elif mode in ["LU", "LD", "RU", "RD"]:
            # x = j*nc + i

            if mode == "LU":
                rangeI = left_to_right
                rangeJ = up_to_down
            elif mode == "LD":
                rangeI = left_to_right
                rangeJ = down_to_up
            elif mode == "RU":
                rangeI = right_to_left
                rangeJ = up_to_down
            else: 
                rangeI = right_to_left
                rangeJ = down_to_up
            for i in rangeI:
                for j in rangeJ:
                    l = len(targets)
                    x = j*nc + i
                    c = unity.cells[x].get_fill_color()
                    if c in [Color("white"),None]:
                        targets.append(x)
                    else:
                        if not l == 0:
                            self.switchCellsPosition(unity,x,targets[currentTarget])
                            targets.append(x)
                            currentTarget += 1


        # Works in all cases --^

    def transferCells(self,unity1,unity2,origin,target,fillColor = BLUE,opacity = 0.3):
        u1 = unity1
        u2 = unity2
        o = origin
        t = target
        l = len(t)
        junk = []
        highLights = []
        if unity1.nColumns == unity2.nColumns and unity1.nRows == unity2.nRows and len(t) == len(o):
            for k in range(l):
                junk.append(u2.cells[t[k]])
                u2.cells[t[k]] = u1.cells[o[k]]
                i = o[k] // u1.nColumns
                j = o[k] % u1.nColumns
                u1.cells[o[k]] = Cell(
                        height=u1.width/u1.nRows,width=u1.width/u1.nColumns,fill_opacity=0).move_to(
                        u1.unitySquare.get_center()
                        +u1.width*(1 - (1+2*(j))/u1.nColumns)/2*LEFT
                        +u1.width*(1 - (1 + 2*(i))/u1.nRows)/2*UP
                    ).set_fill(fillColor,opacity = opacity)

            self.play(
                *[
                    FadeIn(
                        u1.cells[o[i]]
                    )
                    for i in range(l)
                ]
            )
            self.add(
                *[
                u2.cells[t[i]]
                for i in range(l)
                ]
            )
            self.play(
                *[
                    FadeOut(
                        junk[i]
                    )
                    for i in range(l)
                ],
                
                *[
                    ApplyMethod(
                        u2.cells[t[i]].move_to, 
                        junk[i].get_center()
                    )
                    for i in range(l)
                ]
            )
            
        else:
            print("not ok")
    
    def transferDestroyCells(self,unity1,unity2,origin,target,fillColor = BLUE,opacity = 0.3,newColor = BLACK):
        u1 = unity1
        u2 = unity2
        o = origin
        t = target
        l = len(t)
        junk = []
        highLights = []
        if unity1.nColumns == unity2.nColumns and unity1.nRows == unity2.nRows and len(t) == len(o):
            for k in range(l):
                junk.append(u2.cells[t[k]])
                u2.cells[t[k]] = u1.cells[o[k]]
                i = o[k] // u1.nColumns
                j = o[k] % u1.nColumns
                u1.cells[o[k]] = Cell(
                        height=u1.width/u1.nRows,width=u1.width/u1.nColumns,fill_opacity=0).move_to(
                        u1.unitySquare.get_center()
                        +u1.width*(1 - (1+2*(j))/u1.nColumns)/2*LEFT
                        +u1.width*(1 - (1 + 2*(i))/u1.nRows)/2*UP
                    ).set_fill(fillColor,opacity = opacity)

            self.play(
                *[
                    FadeIn(
                        u1.cells[o[i]]
                    )
                    for i in range(l)
                ]
            )
            self.add(
                *[
                u2.cells[t[i]]
                for i in range(l)
                ]
            )
            
            self.play(
                *[
                    FadeOut(
                        junk[i]
                    )
                    for i in range(l)
                ],
                
                *[
                    ApplyMethod(
                        u2.cells[t[i]].moveWhileChangingColor,newColor,junk[i].get_center()
                    )
                    for i in range(l)
                ]
            )

            
            
            
        else:
            print("not ok")

    def partitionateCells(self, unity, targetCells, nr, nc, colorOfParts=[]):
        parts = []
        l = len(targetCells)
        for i in range(l):
            tnum = targetCells[i]
            # get position of nth target
            target_center = unity.cells[tnum].get_center()
            wcell = unity.width/unity.nColumns
            hcell = unity.width/unity.nRows
            wpart = wcell/nc
            hpart = hcell/nr
            colorCell = unity.cells[tnum].get_fill_color()
            # create NR*NC cells assigning positions
            for k in range(nr*nc):
                if colorOfParts != []:
                    colorCell = colorOfParts[k]
                leftUpCornerPos = target_center - (wcell/2)*RIGHT - (hcell/2)*DOWN
                partx = (k%nc)*wpart*RIGHT + (wpart/2)*RIGHT
                party = (k//nc)*hpart*DOWN + (hpart/2)*DOWN
                partcoords = leftUpCornerPos +party+partx
                parts.append(
                    Cell(height=hpart,width=wpart,fill_opacity=0).move_to(
                        partcoords
                    ).set_fill(colorCell,1)
                )
        
        oldCells = []

        for i in range(l):
            oldCells.append(unity.cells[targetCells[i]])
        print(len(unity.cells))
        for i in range(l):
            unity.cells.remove(oldCells[i])

        print(len(unity.cells))
        # fade in new parts AND fade out old cells
        self.play(
            *[
                FadeIn(
                    parts[i]
                )
                for i in range(nr*nc*l)
            ],
            *[
                FadeOut(
                    oldCells[i]
                )
                for i in range(len(oldCells))
            ]
        )
        self.wait(1)
        # fade out new parts
        for i in range(len(parts)):
            unity.cells.append(parts[i])
        print(len(unity.cells))
        
        unity.sortCells()
        
        self.wait(1)

    def highLightBorderCells(self, unity, ns, newStrokeColor=YELLOW):
        newCells = []
        for i in range(len(unity.cells)):
            if i in ns:
                newCells.append( 
                    Cell(height=unity.width/unity.nRows,width=unity.width/unity.nColumns,fill_opacity=0,color=newStrokeColor).move_to(
                        unity.cells[i].get_center()
                    )
                )
            else:
                newCells.append(unity.cells[i])

        self.play(
            *[
                Transform(
                    unity.cells[k],
                    newCells[k]                   
                )
                for k in range(len(unity.cells))
            ]
        )

    def multiplyUnits(self, unityOrigin, unityTarget, targetCells, animation = "TRANSFORMFROMCOPY", premadeColor = ""):
        animation = str(animation).upper()

        uo = unityOrigin
        ut = unityTarget
        tc = targetCells

        uoCenter = uo.unitySquare.get_center()
        uoh = uo.unitySquare.height
        uow = uo.unitySquare.width

        utCenter = ut.unitySquare.get_center()
        uth = ut.unitySquare.height
        utw = ut.unitySquare.width        

        productArray = []
        # loop through every cell in unityTarget
        for i in range(len(tc)):
            utc = ut.cells[tc[i]]
            utcCenter = utc.get_center()
            utcw = utc.width
            utch = utc.height
            utcColor = utc.get_fill_color()

            # create array of positions
            for k in range(len(uo.cells)):
                uoc = uo.cells[k]
                uocw = uoc.width
                uoch = uoc.height
                uocCenter = uoc.get_center()
                
                ct1 = uocCenter - uoCenter
                ct2x = (utcw/uow)*ct1[0]*RIGHT
                ct2y = (utch/uoh)*ct1[1]*UP
                ct2 = ct2x + ct2y

                # Sign rule of multiplication

                uocColor = uoc.get_fill_color()
                prodColor = ""
                if str(utcColor).upper() == str(uocColor).upper():
                    prodColor = BLUE
                else:
                    prodColor = RED

                if str(uocColor) == "white":
                    prodColor = BLACK
                if str(premadeColor) != "":
                    prodColor = premadeColor

                prodPos = utcCenter + ct2
                prodH = (uoch*utch)/uoh
                prodW = (uocw*utcw)/uow

                productArray.append(
                    Cell(height=prodH,width=prodW,fill_opacity=0).move_to(
                        prodPos
                    ).set_fill(prodColor,1)
                )

        if animation == "FADEIN":

            self.play(
                *[
                    FadeIn(
                        productArray[k]
                    )
                    for k in range(len(productArray))
                ]
            )
        
        elif animation == "TRANSFORMFROMCOPY":

            self.play(
                *[
                    TransformFromCopy(
                        uo.cells[k%len(uo.cells)], 
                        productArray[k]
                    )
                    for k in range(len(productArray))
                ]
            )

        elif animation == "TRANSFORMFROMCOPYPAUSING":

            m = len(productArray)//len(uo.cells)

            for j in range(m):
                self.play(
                    *[
                        TransformFromCopy(
                            uo.cells[k], 
                            productArray[j*len(uo.cells)+k]
                        )
                        for k in range(len(uo.cells))
                    ]
                )

        elif animation == "RETURNARRAY":
            return productArray
        else:
            print("Multiply function -> Your animation atribute has no valid animations")



# See old_projects folder for many, many more