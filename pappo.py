from manim import *

class Pappo(MovingCameraScene):
    def construct(self):
        
        circ = Circle(radius=3, color=WHITE).shift(1.5*DOWN)
        p1 = Dot(circ.point_at_angle(0))
        p2 = Dot(circ.point_at_angle(PI))
        p3 = Dot(circ.point_at_angle(PI*5/8))

        tri = always_redraw(lambda: Polygon(
            [p1.get_x(), p1.get_y(), 0],
            [p2.get_x(), p2.get_y(), 0],
            [p3.get_x(), p3.get_y(), 0], color=WHITE
        ))
        
        right_angle = always_redraw(lambda: RightAngle(Line(p1, p3), Line(p2, p3), quadrant=(-1, -1)))

        self.play(
            FadeIn(p1, p2, p3),
            Create(tri, run_time = 3)
        )
        self.play(Create(right_angle), run_time=0.5)
        self.wait()

        pa1 = always_redraw(lambda: Dot([p2.get_x()-(p3.get_y()-p2.get_y()), p2.get_y()+(p3.get_x()-p2.get_x()), 0]))
        pa2 = always_redraw(lambda: Dot([p3.get_x()-(p3.get_y()-p2.get_y()), p3.get_y()+(p3.get_x()-p2.get_x()), 0]))
        a_sq = always_redraw(lambda: Polygon(
            [p2.get_x(), p2.get_y(), 0],
            [p3.get_x(), p3.get_y(), 0],
            [pa2.get_x(), pa2.get_y(), 0],
            [pa1.get_x(), pa1.get_y(), 0], color=GREEN, fill_color=GREEN, fill_opacity=0.8
        ))
        self.play(
            FadeIn(VGroup(pa1, pa2)),
            DrawBorderThenFill(a_sq, run_time=2.5)
        )
        
        self.play(self.camera.frame.animate.set(width=28))

        pb1 = always_redraw(lambda: Dot([p1.get_x()+(p3.get_y()-p1.get_y()), p2.get_y()+(p1.get_x()-p3.get_x()), 0]))
        pb2 = always_redraw(lambda: Dot([p3.get_x()+(p3.get_y()-p1.get_y()), p3.get_y()+(p1.get_x()-p3.get_x()), 0]))
        b_sq = always_redraw(lambda: Polygon(
            [p1.get_x(), p1.get_y(), 0],
            [p3.get_x(), p3.get_y(), 0],
            [pb2.get_x(), pb2.get_y(), 0],
            [pb1.get_x(), pb1.get_y(), 0], color=ORANGE, fill_color=ORANGE, fill_opacity=0.8
        ))
        self.play(
            FadeIn(VGroup(pb1, pb2)),
            DrawBorderThenFill(b_sq, run_time=2.5)
        )

        int = Dot([p3.get_x(), pa2.get_y()+(pb2.get_y()-p3.get_y()), 0])
        line1 = Line(pa2, int)
        line2 = Line(pb2, int)
        line3 = DashedLine(int, p3)
        pm = Dot([p3.get_x(), p1.get_y(), 0])
        pn = Dot([p3.get_x(), pm.get_y()-(int.get_y()-p3.get_y()), 0])
        lmn = DashedLine(pm, pn)

        self.play(
            Create(line1),
            Create(line2),
            FadeIn(int)
        )
        self.wait()
        
        self.play(Create(line3))
        self.wait()
        
        self.play(
            Transform(line3.copy(), lmn), 
            Transform(int.copy(), pm), 
            Transform(p3.copy(), pn)
        )
        self.wait()

        pc1 = Dot([p2.get_x(), pn.get_y(), 0])
        pc2 = Dot([p1.get_x(), pn.get_y(), 0])

        self.play(
            Transform(pn.copy(), pc1), 
            Transform(pn.copy(), pc2), 
            Transform(lmn.copy(), Line(pc1, p2)), 
            Transform(lmn.copy(), Line(pc2, p1)),
            Create(Line(pn, pc1)),
            Create(Line(pn, pc2))
        )
        self.wait()

        c_sq = always_redraw(lambda: Polygon(
            [p2.get_x(), p2.get_y(), 0],
            [pc1.get_x(), pc1.get_y(), 0],
            [pc2.get_x(), pc2.get_y(), 0],
            [p1.get_x(), p1.get_y(), 0], color=BLUE, fill_color=BLUE, fill_opacity=0.8
        ))
        self.play(DrawBorderThenFill(c_sq))
        self.wait()