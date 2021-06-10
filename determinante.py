from big_ol_pile_of_manim_imports import *
from old_projects.eola.chapter6 import *

def apply_matrix(self, matrix, **kwargs):
        """
        Applies the transformation represented by the
        given matrix to the number plane, and each vector/similar
        mobject on it.
        Parameters
        ----------
        matrix (Union[np.ndarray, list, tuple])
            The matrix.
        **kwargs
            Any valid keyword argument of self.apply_transposed_matrix()
        """
        self.apply_transposed_matrix(np.array(matrix).T, **kwargs)

class DrawAnAxis(Scene):
    CONFIG = { "plane_kwargs" : {
    "x_line_frequency" : 3,
    "y_line_frequency" : 3
    }
    }
    
    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())

        self.add(my_plane)
        self.wait()
        
        matrix = [[0, 1], [-1, 0]]
        
        self.apply_matrix(matrix)
        self.wait()
class Matrix2x2:
    def __init__(self, base1, base2, position = 5*RIGHT + 2*UP):
        self.b1 = base1
        self.b2 = base2

        self.v1 = Vector(self.b1).set_fill(GREEN,0.35)
        self.v2 = Vector(self.b2).set_fill(RED,0.35)

        self.matrix = [
            [self.b1[0], self.b2[0]],
            [self.b1[1], self.b2[1]]
        ]
        
        self.det = self.b1[0]*self.b2[1] - self.b2[0]*self.b1[1]
        self.detPos = ((self.b1[0] + self.b2[0])/2)*RIGHT + ((self.b1[1] + self.b2[1])/2)*UP

        if not self.det == 0:
            self.inverse = [
                [self.b2[1]/self.det, -self.b2[0]/self.det],
                [-self.b1[1]/self.det, self.b1[0]/self.det]
            ]

        self.latex = self.get_matrix_latex(self.matrix)
        self.position = position

        self.p = Polygon(
            0*RIGHT + 0*UP,
            self.b1[0]*RIGHT + self.b1[1]*UP,
            (self.b1[0] + self.b2[0])*RIGHT +  (self.b1[1] + self.b2[1])*UP,
            self.b2[0]*RIGHT + self.b2[1]*UP
        )
        self.p.set_fill(YELLOW, 0.2)
        self.p.set_stroke(YELLOW, 1)

    def get_matrix_latex(self, m):
        begin = "\\begin{bmatrix}"
        end = "\end{bmatrix}"
        latext = ""

        nc = len(m[0])
        nr = len(m)

        latext += begin
        for i in range(nr):
            for j in range(nc):
                latext+=str(m[i][j]) + " "
                if not j == nc-1 : 
                    latext+="& "
            if not i == nr-1 :
                latext+="\\\ "
        latext+=end
        return latext
class Vetor:
    def __init__(self, pos, label):
        self.pos = pos
        self.label = "\\vec{ " + label + " }"
        self.v = Vector(self.pos)

        mForm = "\\begin{bmatrix}"
        vForm = "("
        for i in range(len(pos)):
            mForm += str(pos[i])
            vForm += str(pos[i])
            if not i == (len(pos) - 1):
                mForm += " \\\ "
                vForm += ", \\ "
        mForm+="\\end{bmatrix}"
        vForm += ")"
        self.mForm = mForm
        self.vForm = vForm

        

class Determinante(LinearTransformationScene):
    CONFIG = {
        "show_coordinates" : True,
        "transposed_matrix" : [[3, 0], [0, 2]]
    }
    def construct(self):
        
        self.add_title("Exercício 11")
        """v = [1,-2]
        u = [1,0]"""

        
        v = [3,0]
        u = [0,3]

        vColor = GREEN
        uColor = RED

        m1 = Matrix2x2(v,u)
        m2 = Matrix2x2([1,0],[0,1])
        
        mlatex = "\\begin{bmatrix} 1 & 0 \\\  0 & 1" + "\\end{bmatrix}"
        m1Tex = TexMobject(mlatex).move_to(m1.position)
        self.wait()
        self.play(
            Write(m1Tex),
        )
        self.apply_matrix(m1.matrix)
        
        self.play(
            FadeIn(m1.p),
            Transform(m1Tex,TexMobject(m1.latex).move_to(m1.position))
        )
        self.wait()

        ptest = TexMobject(str("3^2 = 9"))
        self.wait()
        self.play(
            Write(ptest.move_to(m1.detPos))
        )

class Abertura(Scene):
    def construct(self):
        titulo = TextMobject("Determinantes",tex_to_color_map={"Determinantes": BLUE})
        titulo.scale(1.5)
        autor = TextMobject("por Iaago Ariel")
        self.play(Write(titulo.move_to(UP)))
        self.wait()
        self.play(Write(autor.move_to(titulo.get_center() + 2*DOWN)))  
        self.wait(2)
        self.play(Uncreate(titulo))
        self.play(Uncreate(autor))
        self.wait()

class OQNVaiVer(Scene):
    def construct(self):
        defForm = "det(A) = \\sum \\pm \\alpha_{1 \\alpha} \\beta_{2 \\beta} \\gamma_{3 \\gamma} \\dots \\alpha_{n \\omega}"
        TextMobject("Você não vai ver:")
        self.wait()
        self.play(Write(TexMobject(defForm).move_to(UP)))
        self.wait()
        self.play(Write(TextMobject("Regra de Sarrus")))
        self.wait()
        self.play(Write(TextMobject("Regra de Crammer").move_to(DOWN)))
        self.wait()
        self.play(ShowCreation(
            Line(3*LEFT+UP,3*RIGHT+DOWN).set_stroke(RED,3)
        ))
        self.play(ShowCreation(
            Line(3*LEFT+DOWN,3*RIGHT+UP).set_stroke(RED,3)
        ))
        self.wait()

class OQVaiVer(Scene):
    def construct(self):
        animVis = "Animação Visual"
        IntGeo = ["Intuição Geométrica","do determinante"]
        self.play(Write(TextMobject(animVis).move_to(UP)))
        self.wait()
        self.play(
            Write(TextMobject(IntGeo[0]).move_to(1*DOWN)),
            Write(TextMobject(IntGeo[1]).move_to(1.5*DOWN))
        )
        self.wait()
        self.clear()
        self.wait()
        self.play(FadeIn(TextMobject("Vamos começar do começo...")))
        self.wait()
        self.clear()
        self.wait()
        VeB = TextMobject("Vetores e Bases")
        self.play(Write(VeB))
        self.wait()
        self.play(Write(TextMobject("...").next_to(VeB,RIGHT).shift(0.1*DOWN + 0.1*LEFT)))
        self.wait()

class DoComeco(Scene):
    def construct(self):
        v = Vetor(UP,"v")
        print(v.mForm)
        self.add(
            TexMobject(v.label + " = ",hex_to_color_map={str(v.pos[0]):RED}).move_to(2.5*LEFT),
            TexMobject(v.vForm + " = "),
            TexMobject(v.mForm).move_to(2.5*RIGHT)
        )
        self.wait()


    