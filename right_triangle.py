from manim import *

class Tri(MovingCameraScene):
    def construct(self):

        circ = Circle(radius=2.5, color=WHITE)

        center = Dot(circ.get_center())
        p1 = Dot(circ.point_at_angle(0))
        p2 = Dot(circ.point_at_angle(PI))
        diam = Line(p2, p1)
        p3 = p1.copy()

        tri = always_redraw(lambda: Polygon(
            [p1.get_x(), p1.get_y(), 0],
            [p2.get_x(), p2.get_y(), 0],
            [p3.get_x(), p3.get_y(), 0], color=WHITE
        ))

        self.play(FadeIn(center))
        self.wait(0.5)
        self.play(Create(circ))
        self.play(FadeIn(p1, p2))
        self.play(Create(diam), run_time=0.8)
        self.wait()
        self.add(p3)
        self.add(tri)
        self.remove(diam)
        self.play(FadeOut(center), run_time=0.5)

        self.play(MoveAlongPath(p3, ArcBetweenPoints(start=2.5*RIGHT, end=circ.point_at_angle(PI*5/8), angle=PI*5/8)), rate_func=smooth, run_time=2)

        rightangle = always_redraw(lambda: RightAngle(Line(p1, p3), Line(p2, p3), quadrant=(-1, -1)))
        self.play(Create(rightangle), run_time=0.5)
        self.wait()

        self.play(
            FadeOut(circ), 
            self.camera.frame.animate.move_to(tri).set(width=tri.width *2)
        )