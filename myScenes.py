#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.

class IntuicaoCento(Scene):
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