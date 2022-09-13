from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, env_width=600, env_height=600, high_score=0):
        super().__init__()
        x_pos = env_width // 2 - 50
        y_pos = (env_height // 2) - 40
        self.score = 0
        self.goto(0, y_pos)
        self.high_score = high_score
        self.color('white')
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Courier', 18, 'bold'))
        self.penup()
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Courier', 18, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open('high_scores.txt', mode='w') as file:
                file.write(str(self.score))

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over!', True, align='center', font=('Courier', 25, 'bold'),)