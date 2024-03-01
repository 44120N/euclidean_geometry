from manim import *
config.media_width = "100%"

class MyScene(Scene):
    def construct(self):
        circle = Circle(radius=2.0, color=BLUE)
        square = Square(side_length=2.0, color=RED)
        triangle = Polygon(np.array([-1, 0, 0]), np.array([1, 0, 0]), np.array([0, 2, 0]), color=GREEN)

        circle.set_fill(BLUE, opacity=0.5)
        square.set_fill(RED, opacity=0.5)
        triangle.set_fill(GREEN, opacity=0.5)

        circle.move_to(ORIGIN)
        square.move_to(ORIGIN)
        triangle.move_to(ORIGIN)

        self.play(Create(circle), Create(square), Create(triangle))

        self.play(
            square.animate.shift(1.5*UP + 1.5*RIGHT),
            triangle.animate.shift(1.5*RIGHT),
        )

        self.wait(7)
        self.play(FadeOut(circle), FadeOut(square), FadeOut(triangle))

class EuclidScene(Scene):
    def construct(self):
        radius=3.0
        circle_A = Circle(radius=radius, color=BLUE)
        circle_B = Circle(radius=radius, color=RED)
        circle_A.set_fill(BLUE, opacity=0.5)
        circle_B.set_fill(RED, opacity=0.5)
        circle_A.move_to(ORIGIN)
        circle_B.move_to(ORIGIN)

        self.play(Create(circle_A))
        self.play(circle_A.animate.shift(1.5*LEFT))
        self.play(Create(circle_B))
        self.play(circle_B.animate.shift(1.5*RIGHT))
        
        intersection = circle_A.point_from_proportion(1/6)
        vertices = np.array([[-1.5,0,0], intersection, [1.5,0,0]])
        triangle = Polygon(*vertices, color=PURPLE)
        triangle.set_fill(PURPLE, opacity=0.8)
        
        label_A = MathTex(r"A").next_to(vertices[0], direction=LEFT)
        label_B = MathTex(r"B").next_to(vertices[2], direction=RIGHT)
        label_GAMMA = MathTex(r"\Gamma").next_to(vertices[1], direction=UP)
        label_DELTA = MathTex(r"\Delta").next_to([-4.5,0,0], direction=RIGHT)
        label_EPSILON = MathTex(r"E").next_to([4.5,0,0], direction=LEFT)
        
        self.play(Create(triangle), Write(label_A), Write(label_B), 
                  Write(label_GAMMA), Write(label_DELTA), Write(label_EPSILON))

        self.wait(10)
        self.play(FadeOut(circle_A), FadeOut(circle_B), FadeOut(triangle), 
                  FadeOut(label_A), FadeOut(label_B), 
                  FadeOut(label_GAMMA), FadeOut(label_DELTA), FadeOut(label_EPSILON))