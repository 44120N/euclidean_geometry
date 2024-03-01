from manim import *
config.media_width = "100%"

class MyRectangle(Scene):
    def construct(self):
        vertices = np.array([
            [-5, -3, 0],
            [5, -3, 0],
            [5, 3, 0],
            [-5, 3, 0],
        ])
        
        rectangle = Polygon(*vertices, color=ORANGE)
        rectangle.set_fill(ORANGE, opacity=0.5)
        
        label_A = MathTex(r"A").next_to(vertices[0], LEFT+DOWN)
        label_B = MathTex(r"B").next_to(vertices[1], RIGHT+DOWN)
        label_C = MathTex(r"C").next_to(vertices[2], RIGHT+UP)
        label_D = MathTex(r"D").next_to(vertices[3], LEFT+UP)
        
        mid_AB = (vertices[0] + vertices[1])/2
        mid_BC = (vertices[1] + vertices[2])/2
        label_l = MathTex(r"l").next_to(mid_AB, direction=DOWN, buff=0.25)
        label_w = MathTex(r"w").next_to(mid_BC, direction=RIGHT, buff=0.25)
        
        self.play(Create(rectangle), Write(label_A), Write(label_B), Write(label_C), Write(label_D), Write(label_l), Write(label_w))
        self.wait(30)
        self.play(FadeOut(rectangle), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_D), FadeOut(label_l), FadeOut(label_w))

class MyRectangle_line(Scene):
    def construct(self):
        vertices = np.array([
            [-5, -3, 0],
            [5, -3, 0],
            [5, 3, 0],
            [-5, 3, 0],
        ])
        
        rectangle = Polygon(*vertices, color=ORANGE)
        
        label_A = MathTex(r"A").next_to(vertices[0], LEFT+DOWN)
        label_B = MathTex(r"B").next_to(vertices[1], RIGHT+DOWN)
        label_C = MathTex(r"C").next_to(vertices[2], RIGHT+UP)
        label_D = MathTex(r"D").next_to(vertices[3], LEFT+UP)
        
        mid_AB = (vertices[0] + vertices[1])/2
        mid_BC = (vertices[1] + vertices[2])/2
        label_l = MathTex(r"l").next_to(mid_AB, direction=DOWN, buff=0.25)
        label_w = MathTex(r"w").next_to(mid_BC, direction=RIGHT, buff=0.25)
        
        self.play(Create(rectangle), Write(label_A), Write(label_B), Write(label_C), Write(label_D), Write(label_l), Write(label_w))
        self.wait(30)
        self.play(FadeOut(rectangle), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_D), FadeOut(label_l), FadeOut(label_w))

class MyRectangle_d(Scene):
    def construct(self):
        vertices = np.array([
            [-5, -3, 0],
            [5, -3, 0],
            [5, 3, 0],
            [-5, 3, 0],
        ])
        
        rectangle = Polygon(*vertices, color=ORANGE)
        rectangle.set_fill(ORANGE, opacity=0.5)
        
        label_A = MathTex(r"A").next_to(vertices[0], LEFT+DOWN)
        label_B = MathTex(r"B").next_to(vertices[1], RIGHT+DOWN)
        label_C = MathTex(r"C").next_to(vertices[2], RIGHT+UP)
        label_D = MathTex(r"D").next_to(vertices[3], LEFT+UP)
        
        mid_AB = (vertices[0] + vertices[1])/2
        mid_BC = (vertices[1] + vertices[2])/2
        label_l = MathTex(r"l").next_to(mid_AB, direction=DOWN, buff=0.25)
        label_w = MathTex(r"w").next_to(mid_BC, direction=RIGHT, buff=0.25)
        
        diagonal = Line(vertices[0], vertices[2], color=ORANGE)
        mid_d = (vertices[0] + vertices[2])/2
        label_d = MathTex(r"d").next_to(mid_d, direction=UP, buff=0.25)
        
        self.play(Create(rectangle), Create(diagonal), Write(label_A), Write(label_B), Write(label_C), Write(label_D), Write(label_l), Write(label_w), Write(label_d))
        self.wait(30)
        self.play(FadeOut(rectangle), FadeOut(diagonal), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_D), FadeOut(label_l), FadeOut(label_w), FadeOut(label_d))