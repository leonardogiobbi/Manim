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
        self.play(FadeOut(angle, run_time=0.2))
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
        self.play(Rotate(VGroup(d1c1, d2c1, d3c1),90*DEGREES,about_point=mid_point))

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

        text = MathTex(
            "c^2", "=", "4 \\cdot \\frac{ab}{2}", "+", "(b-a)^2"
        ).shift(2.5*RIGHT+1.5*DOWN).scale(1.5)

        self.play(Transform(c2, text[0]))
        self.play(Write(text[1]))
        self.play(FadeOut(c_square, c_ticks))

        tric = Polygon(
            [d1.get_x(), d1.get_y(), 0], 
            [d2.get_x(), d2.get_y(), 0], 
            [d3.get_x(), d3.get_y(), 0]
            ).set_fill(color=BLUE, opacity=0.8)
        tri1c = tri1.copy().set_fill(color=BLUE, opacity=0.8)
        tri2c = tri2.copy().set_fill(color=BLUE, opacity=0.8)
        tri3c = tri3.copy().set_fill(color=BLUE, opacity=0.8)

        self.play(FadeIn(tric, run_time=0.3), FadeOut(a, b, cc, run_time=0.3))
        self.play(FadeIn(tri1c, run_time=0.3))
        self.play(FadeIn(tri2c, run_time=0.3))
        self.play(FadeIn(tri3c, run_time=0.3))

        ab2 = VGroup(
            MathTex("\\frac{ab}{2}").move_to(tric.get_center_of_mass()),
            MathTex("\\frac{ab}{2}").move_to(tri1c.get_center_of_mass()),
            MathTex("\\frac{ab}{2}").move_to(tri2c.get_center_of_mass()),
            MathTex("\\frac{ab}{2}").move_to(tri3c.get_center_of_mass()),
        )

        self.play(Write(ab2))
        self.play(Transform(ab2, text[2]))
        
        self.play(FadeOut(VGroup(tric, tri1c, tri2c, tri3c)), FadeIn(a, b, cc))

        midsq = Polygon(
            [d1.get_x(), d1.get_y(), 0],
            [d1c1.get_x(), d1c1.get_y(), 0],
            [d1c2.get_x(), d1c2.get_y(), 0],
            [d1c3.get_x(), d1c3.get_y(), 0], color=ORANGE, fill_color=ORANGE, fill_opacity=0.8
        )

        self.play(DrawBorderThenFill(midsq))

        self.play(Write(text[3]), Transform(midsq, text[4]))

        self.wait()

        self.play(self.camera.frame.animate.set(width=text.width+5).move_to(text))

        self.wait()

        self.play(
            Transform(ab2, Tex("2ab").move_to(text[2]).scale(1.5))
            )
 
        self.play(
            Transform(midsq, MathTex("b^2 - 2ab + a^2").move_to(text[4]).scale(1.5).shift(RIGHT)), 
            self.camera.frame.animate.shift(RIGHT)
            )

        self.wait(1.2)

        self.play(
            Transform(VGroup(ab2, text[3], midsq), MathTex("a^2 + b^2").move_to(text[2]).scale(1.5).shift(0.5*RIGHT)), 
            self.camera.frame.animate.shift(2.5*LEFT).set(width=text.width+3)
            )

        self.wait()