from manim import *

class Bhaskara(MovingCameraScene):
    def construct(self):
        
        # punti
        d1 = Dot([-1.5, -2, 0]) #A
        d2 = Dot([1.5, -2, 0]) #B
        d3 = Dot([-1.5, 2, 0]) #C

        # lati triangolo
        tri_side1 = always_redraw(lambda: Line(d3, d1))
        tri_side2 = always_redraw(lambda: Line(d1, d2))
        tri_side3 = always_redraw(lambda: Line(d2, d3))
        tri = always_redraw(lambda: Polygon(
            [d1.get_x(), d1.get_y(), 0], 
            [d2.get_x(), d2.get_y(), 0], 
            [d3.get_x(), d3.get_y(), 0]
            ))

        # testo ABC
        a = always_redraw(lambda: Tex('a').next_to(tri_side2.get_midpoint(), UP))
        b = always_redraw(lambda: Tex('b').next_to(tri_side1.get_midpoint()))
        c = always_redraw(lambda: Tex('c').next_to(tri_side3.get_midpoint()))

        #angolo retto
        angle = RightAngle(tri_side2, tri_side1, quadrant=(1, -1))

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
        self.play(Create(angle), run_time=0.4)

        self.wait()

        # lati e punto rotazione
        length_b = (d3.get_y()-d1.get_y())
        length_a = (d2.get_x()-d1.get_x())
        dc1 = always_redraw(lambda: Dot([d1.get_x(), (d1.get_y()+(length_b-length_a)), 0]).scale(0.8))
        dc2 = always_redraw(lambda: Dot([(d1.get_x()-(length_b-length_a)), d1.get_y(), 0]).scale(0.8))
        mid_point = Line(dc1, dc2).get_midpoint()

        # riduci
        self.play(self.camera.frame.animate.set(width=20).move_to(mid_point))
        self.wait()
        
        # prima copia triangolo
        d1c1 = d1.copy()
        d2c1 = d2.copy()
        d3c1 = d3.copy()
        tri1 = always_redraw(lambda: Polygon(
            [d1c1.get_x(), d1c1.get_y(), 0], 
            [d2c1.get_x(), d2c1.get_y(), 0], 
            [d3c1.get_x(), d3c1.get_y(), 0], color=WHITE
            ))
        # prima rotazione
        self.add(VGroup(d1c1, d2c1, d3c1))
        self.add(tri1)
        self.play(Rotate(VGroup(d1c1, d2c1, d3c1),90*DEGREES,about_point=mid_point), FadeOut(angle, run_time=0.3))

        # seconda copia triangolo
        d1c2 = d1c1.copy()
        d2c2 = d2c1.copy()
        d3c2 = d3c1.copy()
        tri2 = always_redraw(lambda: Polygon(
            [d1c2.get_x(), d1c2.get_y(), 0], 
            [d2c2.get_x(), d2c2.get_y(), 0], 
            [d3c2.get_x(), d3c2.get_y(), 0], color=WHITE
            ))
        # seconda rotazione
        self.add(VGroup(d1c2, d2c2, d3c2))
        self.add(tri2)
        self.play(Rotate(VGroup(d1c2, d2c2, d3c2),90*DEGREES,about_point=mid_point))

        # terza copia triangolo
        d1c3 = d1c2.copy()
        d2c3 = d2c2.copy()
        d3c3 = d3c2.copy()
        tri3 = always_redraw(lambda: Polygon(
            [d1c3.get_x(), d1c3.get_y(), 0], 
            [d2c3.get_x(), d2c3.get_y(), 0], 
            [d3c3.get_x(), d3c3.get_y(), 0], color=WHITE
            ))
        # terza rotazione
        self.add(VGroup(d1c3, d2c3, d3c3))
        self.add(tri3)
        self.play(Rotate(VGroup(d1c3, d2c3, d3c3),90*DEGREES,about_point=mid_point))

        self.wait(0.5)

        # shifta a sinistra
        self.play(VGroup(
            d1, d2, d3, d1c1, d1c2, d1c3, d2c1, d2c2, d2c3, d3c1, d3c2, d3c3
            ).animate.shift(5.5*LEFT))
    
        # crea quadrato c
        ds1 = d3.copy()
        ds2 = d3c1.copy()
        ds3 = d3c2.copy()
        ds4 = d3c3.copy()
        c_square = Polygon(
            [ds1.get_x(), ds1.get_y(), 0],
            [ds2.get_x(), ds2.get_y(), 0],
            [ds3.get_x(), ds3.get_y(), 0],
            [ds4.get_x(), ds4.get_y(), 0], color=RED, fill_color=RED, fill_opacity=1
        )

        c_ticks = VGroup(
            Tex('c').next_to(Line(ds1, ds2).get_midpoint(), LEFT),
            Tex('c').next_to(Line(ds2, ds3).get_midpoint(), LEFT),
            Tex('c').next_to(Line(ds3, ds4).get_midpoint())
            )

        self.play(
            DrawBorderThenFill(c_square),
            Write(c_ticks)
        )

        c2 = MathTex('c^2').move_to(c_square.get_center())
        self.play(Write(c2))
        
        cc = Tex('c').move_to(c.get_center())
        self.add(cc)
        self.remove(c)

        equal = Tex(' = ').next_to(ds4, buff=1)
        self.play(Write(equal))
        
        # shifta a destra
        self.play(VGroup(
            d1, d2, d3, d1c1, d1c2, d1c3, d2c1, d2c2, d2c3, d3c1, d3c2, d3c3
            ).animate.next_to(equal).shift(RIGHT+0.5*UP))
        
        # scritte lati
        b1 = Tex('b').next_to(tri_side1.get_midpoint())
        self.remove(b)
        self.play(b1.animate.next_to(Line(d1c1, d3c1), UP))
        self.add(Tex('a').next_to(tri_side2, UP))
        self.play(FadeOut(VGroup(a, d1c2, d1c3)), run_time=0.3)
        
        # punti quadrato
        sqp1 = d1c1.copy().scale(0.72)
        sqp2 = d1.copy().scale(0.72)
        self.add(sqp1, sqp2)
        self.add(Line(sqp1, d3c1), Line(sqp1, sqp2))

        # ruota triangoli
        self.play(Rotate(VGroup(d1c1, d2c1),270*DEGREES,about_point=d3c1.get_center()))
        self.play(Write(Tex('b').next_to(Line(d1c1, d3c1), LEFT)))
        self.play(Rotate(VGroup(d1, d3),-270*DEGREES,about_point=d3c3.get_center()))
        self.play(Write(Tex('a').next_to(Line(d1, d2))))

        # poligono totale
        quad = Polygon(
            [d3c1.get_x(), d3c1.get_y(), 0], 
            [d1c1.get_x(), d1c1.get_y(), 0], 
            [d1.get_x(), d1.get_y(), 0],
            [d2.get_x(), d2.get_y(), 0],
            [sqp2.get_x(), sqp2.get_y(), 0], 
            [sqp1.get_x(), sqp1.get_y(), 0], color=BLUE, fill_color=BLUE, fill_opacity=0.8
        )
        # self.play(DrawBorderThenFill(quad))
        # fade out
        self.add(quad.copy().set_fill(opacity=0).set_stroke(WHITE))
        self.play(FadeOut(tri1, tri2, tri3, tri_side1, tri_side2, tri_side3, d1, d2, d3, d1c1, d2c1, d2c2, d2c3, d3c1, d3c2, d3c3))
        # self.play(FadeOut(quad))
        
        # quadrato b
        b_square = Polygon(
            [d3c1.get_x(), d3c1.get_y(), 0], 
            [d1c1.get_x(), d1c1.get_y(), 0], 
            [sqp1.get_x(), d1.get_y(), 0],
            [sqp1.get_x(), sqp1.get_y(), 0], color=ORANGE, fill_color=ORANGE, fill_opacity=0.8
        )
        # quadrato a
        a_square = Polygon(
            [sqp2.get_x(), sqp2.get_y(), 0], 
            [sqp1.get_x(), d1.get_y(), 0], 
            [d1.get_x(), d1.get_y(), 0],
            [d2.get_x(), d2.get_y(), 0], color=GREEN, fill_color=GREEN, fill_opacity=0.8
        )

        # colora
        self.play(DrawBorderThenFill(b_square))
        self.play(Write(MathTex('b^2').move_to(b_square.get_center())))
        self.play(DrawBorderThenFill(a_square))
        self.play(Write(MathTex('a^2').move_to(a_square.get_center())))

        self.wait()