from manim import *

class Pitagora(Scene):
    def construct(self):
        
        # punti
        d1 = Dot([-1.5, -2, 0]) #A
        d2 = Dot([1.5, -2, 0]) #B
        d3 = Dot([-1.5, 2, 0]) #C
        
        # lati triangolo
        tri_side1 = always_redraw(lambda: Line(d3, d1))
        tri_side2 = always_redraw(lambda: Line(d1, d2))
        tri_side3 = always_redraw(lambda: Line(d2, d3))
        
        # testo ABC
        a = always_redraw(lambda: Tex('a').next_to(tri_side2.get_midpoint(), DOWN))
        b = always_redraw(lambda: Tex('b').next_to(tri_side1.get_midpoint(), LEFT))
        c = always_redraw(lambda: Tex('c').next_to(tri_side3.get_midpoint()))

        #angolo retto
        line1 = Line(start=[-1.1, -2, 0], end=[-1.1, -1.6, 0])
        line2 = Line(start=[-1.08, -1.6, 0], end=[-1.5, -1.6, 0])

        # vertici quadrato
        ds1 = Dot([2.5, -2, 0])
        ds2 = Dot([2.5, 2, 0])
        # lati quadrato
        sq_side1 = always_redraw(lambda:Line(d3, d1))
        sq_side2 = always_redraw(lambda:Line(d1, ds1))
        sq_side3 = always_redraw(lambda:Line(ds1, ds2))
        sq_side4 = always_redraw(lambda:Line(ds2, d3))

        # punti rotazione
        d1_copy = Dot([-1.5, -2, 0])
        d2_copy = Dot([1.5, -2, 0])
        # lati triangolo ruotato
        tri_side1_copy = always_redraw(lambda: Line(d3, d1_copy))
        tri_side2_copy = always_redraw(lambda: Line(d1_copy, d2_copy))
        tri_side3_copy = always_redraw(lambda: Line(d2_copy, d3))

        # crea punti
        self.play(FadeIn(d1))
        self.play(FadeIn(d2))
        self.play(FadeIn(d3))

        self.wait(0.3)

        # crea triangolo
        self.play(Create(tri_side1))
        self.play(Create(tri_side2))
        self.play(Create(tri_side3))
        self.play(Write(VGroup(a, b, c)))

        self.wait(0.2)

        # crea angolo
        self.play(Create(VGroup(line1, line2)), run_time=0.4)

        self.wait(0.5)

        # muove vertici
        self.play(d2.animate.shift(RIGHT), run_time=0.5)
        self.play(d2.animate.shift(LEFT), run_time=0.5)
        self.play(d3.animate.shift(UP), run_time=0.5)
        self.play(d3.animate.shift(DOWN), run_time=0.5)

        # crea vertici quadrato
        self.play(FadeIn(VGroup(ds1, ds2)), run_time=0.5)
        # crea quadrato
        self.play(Create(sq_side1), run_time=0.7)
        self.play(Create(sq_side2), run_time=0.7)
        self.play(Create(sq_side3), run_time=0.7)
        self.play(Create(sq_side4), run_time=0.7)

        self.wait()

        # crea triangolo da ruotare
        self.add(VGroup(d1_copy, d2_copy))
        self.add(VGroup(tri_side1_copy, tri_side2_copy, tri_side3_copy))

        # shifta figura verso il basso
        self.play(VGroup(d1, d2, d3, ds1, ds2, d1_copy, d2_copy, line1, line2).animate.shift(1.3*DOWN))
        
        self.wait(0.5)

        # ruota triangolo
        self.play(Rotate(VGroup(d1_copy, d2_copy),90*DEGREES,about_point=d3.get_center()))
        self.play(Write(VGroup(
            always_redraw(lambda: Tex('a').next_to(tri_side2_copy.get_midpoint(), RIGHT)), 
            always_redraw(lambda: Tex('c').next_to(tri_side3_copy.get_midpoint(), LEFT)),
            always_redraw(lambda: Tex('b').next_to(sq_side3.get_midpoint(), RIGHT)),
            )))
        self.play(Create(always_redraw(lambda: Line(d2_copy, d2)), run_time=0.7))

        self.wait()

        self.play(VGroup(d1, d2, d3, ds1, ds2, d1_copy, d2_copy, line1, line2).animate.to_edge(LEFT))

        self.wait()
        
        # quadrato BDA'C
        quad = Polygon(
            [d1.get_x(), d1.get_y(), 0], 
            [ds1.get_x(), ds1.get_y(), 0], 
            [ds2.get_x(), ds2.get_y(), 0], 
            [d3.get_x(), d3.get_y(), 0], color= RED, fill_opacity=0.8, fill_color=RED)

        # quadrilatero equivalente
        quad2 = VGroup(
            always_redraw(lambda: Polygon(
            [d2.get_x(), d2.get_y(), 0], 
            [ds1.get_x(), ds1.get_y(), 0],
            [ds2.get_x(), ds2.get_y(), 0], 
            [d3.get_x(), d3.get_y(), 0], 
            color=BLUE, fill_opacity=0.8, fill_color=BLUE)),
            always_redraw(lambda: Polygon(
            [d1_copy.get_x(), d1_copy.get_y(), 0], 
            [d2_copy.get_x(), d2_copy.get_y(), 0],
            [d3.get_x(), d3.get_y(), 0], 
            color=BLUE, fill_opacity=0.8, fill_color=BLUE))        
        )

        # triangolo verde
        quad2_1 = Polygon(
            [d2_copy.get_x(), d2_copy.get_y(), 0], 
            [d2.get_x(), d2.get_y(), 0], 
            [d3.get_x(), d3.get_y(), 0], color=GREEN, fill_opacity=0.8, fill_color=GREEN)

        # triangolo arancione
        quad2_2 = Polygon(
            [d2_copy.get_x(), d2_copy.get_y(), 0], 
            [d2.get_x(), d2.get_y(), 0], 
            [ds1.get_x(), ds1.get_y(), 0], color=ORANGE, fill_opacity=0.8, fill_color=ORANGE)        

        # crea quadrato
        self.play(DrawBorderThenFill(quad))

        # shift + scale quadrato
        self.play(quad.animate.move_to(2*UP+RIGHT).scale(0.4))
        self.play(Write(VGroup(
            Tex('b').next_to(quad.get_edge_center(DOWN), DOWN).scale(0.5), 
            Tex('b').next_to(quad.get_edge_center(LEFT), LEFT).scale(0.5),
            )))
        self.play(Write(MathTex("b^2").move_to(quad.get_center()).scale(0.8)))
        equal = Tex(' =').next_to(quad)
        self.play(Write(equal))

        # ruota avanti indietro
        self.play(DrawBorderThenFill(quad2))
        self.play(Rotate(VGroup(d1_copy, d2_copy),-90*DEGREES,about_point=d3.get_center()))
        self.wait(0.2)
        self.play(Rotate(VGroup(d1_copy, d2_copy),90*DEGREES,about_point=d3.get_center()))
        self.play(FadeOut(quad2))

        # shift + scale quadrato verde 
        self.play(DrawBorderThenFill(quad2_1))
        self.play(quad2_1.animate.next_to(equal, buff=-1).scale(0.4))
        self.play(Write(VGroup(
            Tex('c').next_to(quad2_1.get_edge_center(UP), 0.8*LEFT+1.3*DOWN).scale(0.5), 
            Tex('c').next_to(quad2_1.get_edge_center(LEFT), LEFT+2*UP, buff=-0.5).scale(0.5),
            )))

        plus = Tex(' + ').next_to(quad2_1)
        self.play(Write(plus))

        # shift + scale quadrato arancione         
        self.play(DrawBorderThenFill(quad2_2))
        self.play(quad2_2.animate.next_to(plus).scale(0.4))
        self.play(Write(VGroup(
            Tex('b - a').next_to(quad2_2.get_edge_center(DOWN), DOWN).scale(0.5), 
            Tex('b + a').next_to(quad2_2.get_edge_center(RIGHT), RIGHT, buff=-0.1).scale(0.5),
            )))

        self.wait()

        # formule
        proof_text = MathTex("b^2=\\frac{c^2}{2}+\\frac{b^2 - a^2}{2}").next_to(quad2_1, DOWN, buff=2)
        proof_text2 = MathTex("2b^2=c^2 + b^2 - a^2").next_to(quad2_1, DOWN, buff=2)
        proof_text3 = MathTex("a^2 + b^2=c^2").next_to(quad2_1, DOWN, buff=2)
        self.play(Write(proof_text), run_time=4)
        self.wait(2.5)
        self.play(proof_text.animate)
        self.play(Transform(proof_text, proof_text2), run_time=1.5)
        self.wait(2.5)
        self.play(Transform(proof_text, proof_text3), run_time=1.5)
        self.wait(2)