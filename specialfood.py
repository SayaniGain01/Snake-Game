from turtle import Turtle
import random
import builtins

class SpecialFoodBarTimer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, -270)
        self.color("red")
        self.total_width = 400
        self.step = 1
        self.active = False
        self.remaining = 0

    def start(self, duration_sec=10):
        self.active = True
        self.remaining = duration_sec
        self.clear()
        self.draw_bar()
        self.getscreen().ontimer(self.update_bar, 1000)

    def draw_bar(self):
        self.clear()
        segment_width = 30
        segment_height = 10
        gap = 5
        total_segments = self.total_width // (segment_width + gap)

        visible_segments = int((self.remaining / 10) * total_segments)

        for i in range(visible_segments):
            x = -self.total_width // 2 + i * (segment_width + gap)
            y = -270
            self.draw_segment(x, y, segment_width, segment_height)

    def draw_segment(self, x, y, width, height):
        self.penup()
        self.goto(x, y)
        self.setheading(0)
        self.pendown()
        self.begin_fill()

        radius = height / 2

        # Left semi-circle
        self.forward(radius)
        self.circle(radius, 180)
        self.forward(width - height)
        self.circle(radius, 180)
        self.forward(radius)

        self.end_fill()
        self.penup()

    def update_bar(self):
        if not self.active:
            return
        
        # Check if the game is still on
        if not getattr(builtins, 'game_is_on', False):
            self.active = False
            return  # Keep the bar frozen, do not clear
        
        self.remaining -= 1
        if self.remaining > 0:
            self.draw_bar()
            self.getscreen().ontimer(self.update_bar, 1000)
        else:
            self.clear()
            self.active = False

    def stop(self, clear=True):
        if clear:
            self.clear()
        self.active = False


class Special_food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1.2, stretch_wid=1.2)
        self.color("red")
        self.speed("fastest")
        self.hideturtle()
        self.timer = SpecialFoodBarTimer()
        self.schedule_spawn()

    def schedule_spawn(self):
        delay = random.randint(25000, 50000)
        self.getscreen().ontimer(self.spawn, delay)

    def spawn(self):
        if not getattr(builtins, 'game_is_on', False):
            return
        self.refresh_safe(self.get_snake_segments())
        self.showturtle()
        self.timer.start(10)
        self.after_despawn()

    def after_despawn(self):
        self.getscreen().ontimer(self.remove, 10000)

    def remove(self):
        self.hideturtle()
        self.timer.stop()
        self.schedule_spawn()

    def refresh_safe(self, snake_segments):
        while True:
            x = random.randint(-260, 260)
            y = random.randint(-260, 260)
            too_close = any(segment.distance(x, y) < 20 for segment in snake_segments)
            if not too_close:
                self.goto(x, y)
                break

    def get_snake_segments(self):
        return getattr(builtins, 'snake', []).segments
