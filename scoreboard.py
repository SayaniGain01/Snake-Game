from turtle import Turtle
ALIGNMENT = "center"
FONT = ("OCR A Extended", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def increase_score(self,points=1):
        self.score += points
        self.clear()
        self.update_scoreboard()
    
    
        