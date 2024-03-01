from manim import *
config.media_width = "100%"

class MyCircle(Scene):
    def construct(self):
        circle = Circle(radius=3.0, color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        
        dots = np.array([[0, 0, 0], [3, 0, 0]])
        r = Line(dots[0], dots[1])
        
        label_O = MathTex(r"O").next_to(dots[0], DOWN)
        label_A = MathTex(r"A").next_to(dots[1], RIGHT+DOWN)
        
        mid_OA = (dots[0]+dots[1])/2
        label_r = MathTex(r"r").next_to(mid_OA, direction=DOWN, buff=0.25)
        
        self.play(Create(circle))
        self.play(Create(r), Write(label_A), Write(label_O), Write(label_r))
        self.wait(30)
        self.play(FadeOut(circle), FadeOut(r), FadeOut(label_A), FadeOut(label_O), FadeOut(label_r))
        
class MyCircle_line(Scene):
    def construct(self):
        circle = Circle(radius=3.0, color=BLUE)
        
        dots = np.array([[0, 0, 0], [3, 0, 0]])
        r = Line(dots[0], dots[1])
        
        label_O = MathTex(r"O").next_to(dots[0], DOWN)
        label_A = MathTex(r"A").next_to(dots[1], RIGHT+DOWN)
        
        mid_OA = (dots[0]+dots[1])/2
        label_r = MathTex(r"r").next_to(mid_OA, direction=DOWN, buff=0.25)
        
        self.play(Create(circle))
        self.play(Create(r), Write(label_A), Write(label_O), Write(label_r))
        self.wait(30)
        self.play(FadeOut(circle), FadeOut(r), FadeOut(label_A), FadeOut(label_O), FadeOut(label_r))

class MyCircle_d(Scene):
    def construct(self):
        circle = Circle(radius=3.0, color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        
        dots = np.array([[0, 0, 0], [3, 0, 0]])
        r = Line(dots[0], dots[1])

        diameter_start = circle.point_from_proportion(0.125)
        diameter_end = circle.point_from_proportion(0.625) 
        diameter = Line(diameter_start, diameter_end, color=BLUE)
        
        label_O = MathTex(r"O").next_to(dots[0], DOWN)
        label_A = MathTex(r"A").next_to(dots[1], RIGHT+DOWN)
        label_B = MathTex(r"B").next_to(diameter_end, LEFT+DOWN)
        label_C = MathTex(r"C").next_to(diameter_start, RIGHT+UP)
        
        label_d = MathTex(r"d").next_to([0, 0, 0], direction=UP, buff=0.25)
        mid_OA = (dots[0] + dots[1]) / 2
        label_r = MathTex(r"r").next_to(mid_OA, direction=DOWN, buff=0.25)
        
        self.play(Create(circle))
        self.play(Create(r), Write(label_A), Write(label_O), Write(label_r))
        self.play(Create(diameter), Write(label_B), Write(label_C), Write(label_d))
        self.wait(30)
        self.play(FadeOut(circle), FadeOut(r), FadeOut(label_A), FadeOut(label_O), FadeOut(label_r), 
                  FadeOut(diameter), FadeOut(label_A), FadeOut(label_O), FadeOut(label_r),
                  FadeOut(label_B), FadeOut(label_C), FadeOut(label_d))