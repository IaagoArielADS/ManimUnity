#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *
from unity import Unity

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.

class CoorArithmetic(Scene):
    def construct(self):
        for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))

        circle = Circle(color=RED, radius=0.5)
        self.add(circle)
        self.wait(0.5)

        aliases = {
            "LEFT * 3": LEFT * 3,
            "UP + RIGHT / 2": UP + RIGHT / 2,
            "DOWN + LEFT * 2": DOWN + LEFT * 2,
            "RIGHT * 3.75 * DOWN": RIGHT * 3.75 * DOWN,
            # certain arithmetic won't work as you expected
            # In [4]: RIGHT * 3.75 * DOWN
            # Out[4]: array([ 0., -0.,  0.])
            "RIGHT * 3.75 + DOWN": RIGHT * 3.75 + DOWN}

        for text, aliase in aliases.items():
            anno = TexMobject(f"\\texttt{{{text}}}")
            self.play(Write(anno, run_time=0.2))
            self.play(ApplyMethod(circle.shift, aliase))
            self.wait(0.2)
            self.play(FadeOut(anno, run_time=0.2))

class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange_submobjects(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(FadeOutAndShiftDown, basel),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            Write(grid),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange_submobjects(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()


class FirstScene(Scene):
    def construct(self):
        textPorcentagem=TexMobject(
            "porcentagem",
            tex_to_color_map={"centagem":BLUE}
        )
        textPorcentagem2=TexMobject(
            "por 100",
            tex_to_color_map={"100":BLUE}
        )
        textPorcentagem3=TexMobject(
            "\\frac{1}{100}",
            tex_to_color_map={"100":BLUE}
        )
        textPorcentagem4=TexMobject(
            "\\% = \\frac{1}{100}",
            tex_to_color_map={"100":BLUE}
        )
        self.play(FadeIn(textPorcentagem))
        self.wait(3)
        self.play(Transform(textPorcentagem,textPorcentagem2));
        self.wait(3)
        self.play(Transform(textPorcentagem,textPorcentagem3));
        self.wait(3)
        self.play(Transform(textPorcentagem,textPorcentagem4));
        self.wait(3)

class Equation:
    def update_operator(self,obj):
        obj.next_to(self.LSide,RIGHT,buff=SMALL_BUFF)

    def update_RSide(self,obj):
        obj.next_to(self.operator,RIGHT,buff=SMALL_BUFF)

    def __init__(self, LSide, operator,RSide):
        self.LSide = TexMobject(LSide)
        self.operator = TexMobject(operator)
        self.RSide = TexMobject(RSide)
        
        

        self.operator.add_updater(self.update_operator)
        self.RSide.add_updater(self.update_RSide)


    def transformLSide(self,result,term = " ",color = WHITE):
        oldLSide = self.LSide
        self.LSide = TexMobject(result,tex_to_color_map={term:color})
        self.operator.add_updater(self.update_operator)
        self.RSide.add_updater(self.update_RSide)
        return Transform(
            oldLSide,
            self.LSide
        )

    def transformRSide(self,result,term = " ",color = WHITE):
        oldRSide = self.RSide
        self.RSide = TexMobject(result,tex_to_color_map={term:color})
        self.operator.add_updater(self.update_operator)
        self.RSide.add_updater(self.update_RSide)
        return Transform(
            oldRSide,
            self.RSide
        )


class IntuicaoCento(Scene):
    def construct(self):
        eq = Equation(
            "144",
            "\\Rightarrow",
            "\\text{cento e quarenta e quatro}"
        )

        self.play(
            FadeIn(
                eq.LSide
            )
        )
        self.wait()
        self.play(
            FadeIn(eq.operator),
            FadeIn(eq.RSide)
        )
        self.wait()
        self.play(
            eq.transformLSide("100 + 44")
        )
        self.wait()
        self.play(
            eq.transformLSide("100 + 44","100",BLUE),
            eq.transformRSide("\\text{cento e quarenta e quatro}","cento",BLUE)
        )
        
class Teste(Scene):
    def construct(self):
        texts = [
            TexMobject("144"),
            TexMobject("\\Leftrightarrow"),
            TexMobject("\\text{cento ","e quarenta e quatro}"),
            TexMobject("100"," + 44"),
            TextMobject("100 + 44",tex_to_color_map={"100 + 44":BLUE}),
        ]
        intro = TextMobject("Porcentagem")
        autor = TextMobject("por Iaago Ariel")
        self.play(
            Write(intro)
        )
        self.wait(2)
        self.play(
            Write(autor.next_to(intro,DOWN,buff=1))
        )
        self.wait(2)
        self.play(
            FadeOut(intro),
            FadeOut(autor)
        )
        self.wait()
        #Line 1
        self.play(Write(texts[0].to_edge(LEFT,buff=4))) # 144
        self.wait(5)
        
        #Line 2
        texts[1].add_updater(lambda m: m.next_to(texts[0]))
        self.play(
            Write(texts[1]) # =>
        )
        self.wait(0.35)
        texts[2].add_updater(lambda m: m.next_to(texts[1]))
        self.play(
            Write(texts[2].next_to(texts[1])), # cento e quarenta e quatro
        )
        self.wait(5)
        
        #Line 3
        self.play(
            Transform(texts[0],texts[3].to_edge(LEFT,buff=4)) # 144 -> 100 + 44 
        )
        self.wait()

        #Line 4
        self.play(
            Transform(texts[0],TexMobject("100"," + 44", tex_to_color_map={"100":BLUE,"44":YELLOW}).to_edge(LEFT,buff=4))
        )
        texts[2].add_updater(lambda m: m.next_to(texts[1]))
        self.play(
            Transform(
                texts[2],
                TexMobject("\\text{cento ","e quarenta e quatro}", tex_to_color_map={"cento":BLUE,"quarenta e quatro":YELLOW}).next_to(texts[1])
            )
        )
        self.wait()

        #Line 5
        self.play(
            FadeOut(texts[0][2]),
            FadeOut(texts[2][3])
        )
        self.wait()
        self.play(
            FadeOut(texts[0][1]),
            FadeOut(texts[2][2])
        )
        self.wait()

        #Line 6
        texts[1].clear_updaters()
        self.play(
            texts[1].shift,0.5*LEFT
        )
        self.wait(3)
        #Line 7
        self.play(
            Transform(texts[0][0],TexMobject("\\over ",".100 ",tex_to_color_map={"\\over":YELLOW,".100":BLUE}).to_edge(LEFT,buff=4)),
            Transform(texts[2][1],TexMobject("\\text{por cento}",tex_to_color_map={"por":YELLOW,"cento":BLUE}).next_to(texts[1],RIGHT,buff=SMALL_BUFF))
        )
        self.wait(5)
        #Line 8
        self.play(
            Transform(texts[0][0],TexMobject("\\over ",".100 ",tex_to_color_map={"\\over":WHITE,".100":WHITE}).to_edge(LEFT,buff=4)),
            Transform(texts[2][1],TexMobject("\\text{por cento}",tex_to_color_map={"por":WHITE,"cento":WHITE}).next_to(texts[1],RIGHT,buff=SMALL_BUFF))
        )
        self.wait(2)
        #Line 9
        self.play(
            Transform(texts[0][0],TexMobject("1","\\over ",".100 ").to_edge(LEFT,buff=4)),
            Transform(texts[2][1],TexMobject("\\text{1 porcento}").next_to(texts[1],RIGHT,buff=SMALL_BUFF))
        )
        self.wait()
        #Line 10
        self.play(
            Transform(texts[0][0],TexMobject("2","\\over ",".100 ").to_edge(LEFT,buff=4)),
            Transform(texts[2][1],TexMobject("\\text{2 porcento}").next_to(texts[1],RIGHT,buff=SMALL_BUFF))
        )
        self.wait(0.35)
        self.play(
            Transform(texts[0][0],TexMobject("20","\\over ",".100 ").to_edge(LEFT,buff=4)),
            Transform(texts[2][1],TexMobject("\\text{20 porcento}").next_to(texts[1],RIGHT,buff=SMALL_BUFF))
        )
        self.wait(0.35)
        self.play(
            Transform(texts[0][0],TexMobject("100","\\over ",".100 ").to_edge(LEFT,buff=4)),
            Transform(texts[2][1],TexMobject("\\text{100 porcento}").next_to(texts[1],RIGHT,buff=SMALL_BUFF))
        )
        self.wait(0.35)
        self.play(
            Transform(texts[0][0],TexMobject("x","\\over ",".100 ").to_edge(LEFT,buff=4)),
            Transform(texts[2][1],TexMobject("x \\text{ porcento}").next_to(texts[1],RIGHT,buff=SMALL_BUFF))
        )

        self.wait(3)
        self.play(
            Write(TexMobject("\\Leftrightarrow x \\%").next_to(texts[2][1],RIGHT,buff=SMALL_BUFF*1.2))
        )
        self.wait(3)
        self.clear()
        self.wait()
        intro = TextMobject("Definição de porcento")
        self.play(
            Write(intro)
        )
        self.wait()
        self.play(
            Write(TexMobject("\\% := ","\\frac{1}{100}").next_to(intro,DOWN, buff=SMALL_BUFF*1.2))
        )
        self.wait(2)

class Teste2(Scene):
    def construct(self):
        texts = TexMobject("144",".","\\Rightarrow","\\text{cento e quarenta e quatro}")
        #Line 1
        self.play(Write(texts[0]))
        self.wait()
        #Line 2
        self.play(
            *[
            Write(texts[i])
            for i in [2,3]
            ]
        )
        self.wait()
        #Line 3
        self.play(
            Transform(texts[0],texts[0].set_color(BLUE))
        )
        self.wait()

class Teste3(Scene):
    def construct(self):
        UNITY_WIDTH = 2
        nColumns = 3
        nRows = 2
        position = -1.25*RIGHT
        position2 = 1.25*RIGHT
        position3 = 3.85*RIGHT
        #u1 = Unity(width=UNITY_WIDTH, nColumns = nColumns, nRows = nRows, position = position, cells=[])
        #u2 = Unity(width=UNITY_WIDTH, nColumns = nColumns, nRows = nRows, position = position2, cells=[])
        #u3 = Unity(width=UNITY_WIDTH, nColumns = nColumns, nRows = nRows, position = position3, cells=[])
        #print(u1.cells == u2.cells)
        
        #u1.highLightCells([8,9,10,11], BLUE)
        #u2.highLightCells([8,9,10,11], BLUE)


        u1 = Unity(width=UNITY_WIDTH, nColumns = 3, nRows = 1, position = position, cells=[])
        u2 = Unity(width=UNITY_WIDTH, nColumns = 4, nRows = 1, position = position2, cells=[])
        u3 = Unity(width=UNITY_WIDTH, nColumns = 1, nRows = 1, position = position3, cells=[])

        u1.highLightCells([0], BLUE)
        u2.highLightCells([0], BLUE)

        self.plotUnity(u1)

        self.play(FadeIn(TextMobject(r"$+$")))

        self.plotUnity(u2)

        self.play(FadeIn(TextMobject("=").move_to(2.55*RIGHT)))

        self.plotUnity(u3)

        self.wait()

        u3 = self.partitionate(u3,"VERTICAL",3)

        self.rotateUnity(u3,90)

        u3 = self.partitionate(u3,"VERTICAL",4)

        u2 = self.partitionate(u2,"HORIZONTAL",3)

        self.rotateUnity(u1,90)

        u1 = self.partitionate(u1,"VERTICAL",4)

        self.wait()

        self.transferCells(u1,u3,[8,9,10,11],[0,1,2,3])
        self.transferCells(u2,u3,[0,4,8],[4,5,6])

        self.wait()

        u1.highLightCells([8,9,10,11], BLUE)
        u2.highLightCells([0,4,8], BLUE)

        self.wait()

        u1 = self.joinPartitions(u1,"VERTICAL",4)

        u2 = self.joinPartitions(u2,"HORIZONTAL",3)

        self.rotateUnity(u1,-90)

        self.wait()

        #u3 = self.partitionate(u3,"VERTICAL",4)
        """
        self.transferCells(u1,u3,[8,9,10,11],[8,9,10,11])
        self.transferCells(u2,u3,[8,9,10,11],[4,5,6,7])

        self.wait()

        u1.highLightCells([8,9,10,11], BLUE)
        u2.highLightCells([8,9,10,11], BLUE)
        
        self.wait()
        
        self.normalizeUnity(u1,"LU")
        self.normalizeUnity(u2,"LU")
        self.normalizeUnity(u3,"LU")

        self.wait()
        """
        #Normalize
        """
        u1.highLightCells([3,5,8,9,10,11,14,19], BLUE)
        self.plotUnity(u1)
        self.wait()
        
        self.wait()
        self.normalizeUnity(u1,"UL")
        """
        #Unity_adding
        """
        self.plotUnity(u1)

        self.play(FadeIn(TextMobject(r"$+$")))

        self.plotUnity(u2)

        self.play(FadeIn(TextMobject("=").move_to(2.55*RIGHT)))

        self.plotUnity(u3)

        self.wait()

        self.transferCells(u1,u3,[8,9,10,11],[8,9,10,11])
        self.transferCells(u2,u3,[8,9,10,11],[4,5,6,7])

        self.wait()

        u1.highLightCells([8,9,10,11], BLUE)
        u2.highLightCells([8,9,10,11], BLUE)
        
        self.wait()
        
        self.normalizeUnity(u1,"LU")
        self.normalizeUnity(u2,"LU")
        self.normalizeUnity(u3,"LU")

        self.wait()
        """
        """
        self.play(
            Transform(
                u1.unitySquare,
                TexMobject(
                    " 4 \\over 12 ",
                    tex_to_color_map={"4":RED}    
                ).move_to(u1.unitySquare.get_center())
            )
        )"""

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

    def shiftUnity(self,unity, position):
        unity.position = unity.position + position
        self.play(
            ApplyMethod(unity.unitySquare.shift, position),
            *[
            ApplyMethod(unity.cells[i].shift, position)
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
                u1.cells[o[k]] = Rectangle(
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


# See old_projects folder for many, many more