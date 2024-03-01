from manim import *
config.media_width = "100%"

class MySquare(Scene):
    def construct(self):
        vertices = np.array([
            [-3, -3, 0],
            [3, -3, 0],
            [3, 3, 0],
            [-3, 3, 0],
        ])
        
        square = Polygon(*vertices, color=RED)
        square.set_fill(RED, opacity=0.5)
        
        label_A = MathTex(r"A").next_to(vertices[0], LEFT+DOWN)
        label_B = MathTex(r"B").next_to(vertices[1], RIGHT+DOWN)
        label_C = MathTex(r"C").next_to(vertices[2], RIGHT+UP)
        label_D = MathTex(r"D").next_to(vertices[3], LEFT+UP)
        
        mid_BC = (vertices[1] + vertices[2])/2
        label_a = MathTex(r"a").next_to(mid_BC, direction=RIGHT, buff=0.25)
        
        self.play(Create(square), Write(label_A), Write(label_B), Write(label_C), Write(label_D), Write(label_a))
        self.wait(30)
        self.play(FadeOut(square), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_D), FadeOut(label_a))

class MySquare_line(Scene):
    def construct(self):
        vertices = np.array([
            [-3, -3, 0],
            [3, -3, 0],
            [3, 3, 0],
            [-3, 3, 0],
        ])
        
        square = Polygon(*vertices, color=RED)
        
        label_A = MathTex(r"A").next_to(vertices[0], LEFT+DOWN)
        label_B = MathTex(r"B").next_to(vertices[1], RIGHT+DOWN)
        label_C = MathTex(r"C").next_to(vertices[2], RIGHT+UP)
        label_D = MathTex(r"D").next_to(vertices[3], LEFT+UP)
        
        mid_BC = (vertices[1] + vertices[2])/2
        label_a = MathTex(r"a").next_to(mid_BC, direction=RIGHT, buff=0.25)
        
        self.play(Create(square), Write(label_A), Write(label_B), Write(label_C), Write(label_D), Write(label_a))
        self.wait(30)
        self.play(FadeOut(square), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_D), FadeOut(label_a))

class MySquare_d(Scene):
    def construct(self):
        vertices = np.array([
            [-3, -3, 0],
            [3, -3, 0],
            [3, 3, 0],
            [-3, 3, 0],
        ])
        
        square = Polygon(*vertices, color=RED)
        square.set_fill(RED, opacity=0.5)
        
        label_A = MathTex(r"A").next_to(vertices[0], LEFT+DOWN)
        label_B = MathTex(r"B").next_to(vertices[1], RIGHT+DOWN)
        label_C = MathTex(r"C").next_to(vertices[2], RIGHT+UP)
        label_D = MathTex(r"D").next_to(vertices[3], LEFT+UP)
        
        mid_BC = (vertices[1] + vertices[2])/2
        label_a = MathTex(r"a").next_to(mid_BC, direction=RIGHT, buff=0.25)
        
        diagonal = Line(vertices[0], vertices[2], color=RED)
        mid_d = (vertices[0] + vertices[2])/2
        label_d = MathTex(r"d").next_to(mid_d, direction=UP, buff=0.25)
        
        self.play(Create(square), Create(diagonal), Write(label_A), Write(label_B), Write(label_C), Write(label_D), Write(label_a), Write(label_d))
        self.wait(30)
        self.play(FadeOut(square), FadeOut(diagonal), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_D), FadeOut(label_a), Write(label_d))