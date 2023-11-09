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
        
        self.score_count = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score_count} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
    def reset(self):
        
        
        self.high_score = int(self.high_score)
        
        if self.score_count > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score_count))
        
        with open("data.txt") as file:
            self.high_score = file.read()
        
            
        self.score_count = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score_count += 1
        self.update_scoreboard()
            