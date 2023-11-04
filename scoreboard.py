from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")



class Scoreboard(Turtle):
    
    def __init__(self):
        
        
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(y=270, x=0)
        
        self.score_count = -1
        self.color("white")
        self.write(arg=f"Score: {self.score_count}", move=False, align=ALIGNMENT, font=FONT)
        self.update_score()
        
       
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font= FONT)
    
        
    def update_score(self):
        self.score_count += 1
        self.clear()
        self.write(arg=f"Score: {self.score_count}", move=False, align="center", font=("Arial", 20, "normal"))
            