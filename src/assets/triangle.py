from manim import *
config.media_width = "100%"

class MyTriangle_abc_line(Scene):
    def construct(self):
        vertices = np.array([[-5, -3, 0], [5, -1, 0], [0, 3, 0]])

        triangle = Polygon(*vertices, color=GREEN)

        label_A = MathTex(r"A").next_to(vertices[0], DOWN)
        label_B = MathTex(r"B").next_to(vertices[1], RIGHT)
        label_C = MathTex(r"C").next_to(vertices[2], UP)
        
        mid_AB = (vertices[0] + vertices[1]) / 2
        mid_BC = (vertices[1] + vertices[2]) / 2
        mid_CA = (vertices[2] + vertices[0]) / 2

        label_a = MathTex(r"a").next_to(mid_BC, direction=UP, buff=0.25)
        label_b = MathTex(r"b").next_to(mid_CA, direction=LEFT, buff=0.25)
        label_c = MathTex(r"c").next_to(mid_AB, direction=DOWN, buff=0.25)

        self.play(Create(triangle), Write(label_A), Write(label_B), Write(label_C), Write(label_a), Write(label_b), Write(label_c))
        self.wait(30)
        self.play(FadeOut(triangle), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_a), FadeOut(label_b), FadeOut(label_c))

class MyTriangle_abc(Scene):
    def construct(self):
        vertices = np.array([[-5, -3, 0], [5, -1, 0], [0, 3, 0]])

        triangle = Polygon(*vertices, color=GREEN)
        triangle.set_fill(GREEN, opacity=0.5)

        label_A = MathTex(r"A").next_to(vertices[0], DOWN)
        label_B = MathTex(r"B").next_to(vertices[1], RIGHT)
        label_C = MathTex(r"C").next_to(vertices[2], UP)
        
        mid_AB = (vertices[0] + vertices[1]) / 2
        mid_BC = (vertices[1] + vertices[2]) / 2
        mid_CA = (vertices[2] + vertices[0]) / 2

        label_a = MathTex(r"a").next_to(mid_BC, direction=UP, buff=0.25)
        label_b = MathTex(r"b").next_to(mid_CA, direction=LEFT, buff=0.25)
        label_c = MathTex(r"c").next_to(mid_AB, direction=DOWN, buff=0.25)

        self.play(Create(triangle), Write(label_A), Write(label_B), Write(label_C), Write(label_a), Write(label_b), Write(label_c))
        self.wait(30)
        self.play(FadeOut(triangle), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_a), FadeOut(label_b), FadeOut(label_c))
        
class MyTriangle_bh(Scene):
    def construct(self):
        vertices = np.array([[-5, -3, 0], [6, -3, 0], [-2, 3, 0]])

        triangle = Polygon(*vertices, color=GREEN)
        triangle.set_fill(GREEN, opacity=0.5)

        height_point = np.array([vertices[2][0], vertices[1][1], 0])
        mid_height = (vertices[2] + height_point) / 2
        mid_base = (vertices[0] + vertices[1]) / 2

        height_line = Line(vertices[2], height_point, color=GREEN)

        right_angle = RightAngle(height_line, Line(vertices[0], vertices[1]), length=0.2, stroke_width=2.5, quadrant=(-1,1))

        label_A = MathTex(r"A").next_to(vertices[0], DOWN)
        label_B = MathTex(r"B").next_to(vertices[1], DOWN)
        label_C = MathTex(r"C").next_to(vertices[2], UP)
        label_h = MathTex(r"h").next_to(mid_height, LEFT, buff=0.1)
        label_b = MathTex(r"b").next_to(mid_base, DOWN, buff=0.1)

        self.play(Create(triangle), Write(label_A), Write(label_B), Write(label_C), Create(height_line), Write(label_h), Write(label_b), Create(right_angle))
        self.wait(30)
        self.play(FadeOut(triangle), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(height_line), FadeOut(label_h), FadeOut(label_b), Create(right_angle))

class Pythagoras(Scene):
    def construct(self):
        square_vertices = np.array([
            [-3.5, -3.5, 0],
            [3.5, -3.5, 0],
            [3.5, 3.5, 0],
            [-3.5, 3.5, 0]
        ])
        
        triangle1_vertices = np.array([
            [-0.5, 3.5, 0],
            [-3.5, 3.5, 0],
            [-3.5, -0.5, 0]
        ])
        
        triangle2_vertices = np.array([
            [-3.5, -0.5, 0],
            [-3.5, -3.5, 0],
            [0.5, -3.5, 0]
        ])
        
        triangle3_vertices = np.array([
            [0.5, -3.5, 0],
            [3.5, -3.5, 0],
            [3.5, 0.5, 0]
        ])
        
        triangle4_vertices = np.array([
            [3.5, 0.5, 0],
            [3.5, 3.5, 0],
            [-0.5, 3.5, 0]
        ])
        
        area_c_vertices = np.array([
            [-0.5, 3.5, 0],
            [-3.5, -0.5, 0],
            [0.5, -3.5, 0],
            [3.5, 0.5, 0]
        ])
        
        square = Polygon(*square_vertices, color=WHITE)
        triangle1 = Polygon(*triangle1_vertices, color=BLUE)
        triangle1.set_fill(BLUE, opacity=0.5)
        triangle2 = Polygon(*triangle2_vertices, color=GREEN)
        triangle2.set_fill(GREEN, opacity=0.5)
        triangle3 = Polygon(*triangle3_vertices, color=BLUE)
        triangle3.set_fill(BLUE, opacity=0.5)
        triangle4 = Polygon(*triangle4_vertices, color=GREEN)
        triangle4.set_fill(GREEN, opacity=0.5)
        
        area_c = Polygon(*area_c_vertices, color=RED)
        area_c.set_fill(RED, opacity=0.5)
        intersect = [0,0,0]
        
        label_a1 = MathTex(r"a").next_to([-2, 3.5, 0], UP, buff=0.1)
        label_b1 = MathTex(r"b").next_to([-3.5, 1.5, 0], LEFT, buff=0.1)
        label_a2 = MathTex(r"a").next_to([-3.5, -2, 0], LEFT, buff=0.1)
        label_b2 = MathTex(r"b").next_to([-1.5, -3.5, 0], DOWN, buff=0.1)
        label_a3 = MathTex(r"a").next_to([2, -3.5, 0], DOWN, buff=0.1)
        label_b3 = MathTex(r"b").next_to([3.5, -1.5, 0], RIGHT, buff=0.1)
        label_a4 = MathTex(r"a").next_to([3.5, 2, 0], RIGHT, buff=0.1)
        label_b4 = MathTex(r"b").next_to([1.5, 3.5, 0], UP, buff=0.1)
        
        label_c1 = MathTex(r"c").next_to([-2, 1.5, 0], UP+LEFT, buff=0.1)
        label_c2 = MathTex(r"c").next_to([-1.5, -2, 0], DOWN+LEFT, buff=0.1)
        label_c3 = MathTex(r"c").next_to([2, -1.5, 0], DOWN+RIGHT, buff=0.1)
        label_c4 = MathTex(r"c").next_to([1.5, 2, 0], UP+RIGHT, buff=0.1)
        label_c = MathTex(r"c^2").next_to(intersect, buff=0)
        
        self.play(Create(square), Create(triangle1), Create(triangle2), Create(triangle3), Create(triangle4),
                  Write(label_a1), Write(label_a2), Write(label_a3), Write(label_a4), 
                  Write(label_b1), Write(label_b2), Write(label_b3), Write(label_b4),
                  Write(label_c1), Write(label_c2), Write(label_c3), Write(label_c4), Write(label_c)
                )
        self.wait(5)
        self.play(FadeOut(label_a1), FadeOut(label_a2), FadeOut(label_a3), FadeOut(label_a4), 
                  FadeOut(label_b1), FadeOut(label_b2), FadeOut(label_b3), FadeOut(label_b4),
                  FadeOut(label_c1), FadeOut(label_c2), FadeOut(label_c3), FadeOut(label_c4), FadeOut(label_c)
                )
        
        triangle2.generate_target()
        triangle3.generate_target()
        triangle4.generate_target()
        pre = 0.5
        
        triangle2.target.shift((3.5-pre)*RIGHT)
        triangle3.target.shift((3.5-pre)*UP + (3.5+pre)*LEFT)
        triangle4.target.shift((3.5+pre)*DOWN)
        self.play(MoveToTarget(triangle2), MoveToTarget(triangle3), MoveToTarget(triangle4))
        self.wait(2)
        
        blue_square_vertices = np.array([
            [-3.5, 3.5, 0],
            [-3.5, -0.5, 0],
            [-0.5, -0.5, 0],
            [-0.5, 3.5, 0]
        ])
        blue_square = Polygon(*blue_square_vertices, color=BLUE)
        blue_square.set_fill(BLUE, opacity=0.5)
        self.remove(triangle1, triangle3)
        self.add(blue_square)
        
        green_square_vertices = np.array([
            [-0.5, -0.5, 0],
            [3.5, -0.5, 0],
            [3.5, -3.5, 0],
            [-0.5, -3.5, 0]
        ])
        green_square = Polygon(*green_square_vertices, color=GREEN)
        green_square.set_fill(GREEN, opacity=0.5)
        self.remove(triangle2, triangle4)
        self.add(green_square)
        
        label_a = MathTex(r"a^2").next_to([-2, -2, 0], buff=0)
        label_b = MathTex(r"b^2").next_to([1.5, 1.5, 0], buff=0)
        
        self.play(Write(label_a), Write(label_b),
                  Write(label_a1), Write(label_a2), 
                  Write(label_b1), Write(label_b4)
                )
        self.wait(2)