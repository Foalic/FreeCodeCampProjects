import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for ball_colour,value in kwargs.items():
            for count in range(value):
                self.contents.append(ball_colour)

    def draw(self, number_of_balls):
        drawn_balls = []
        balls_left = [ball for ball in self.contents]

        if number_of_balls > len(self.contents):
            drawn_balls = self.contents
        else:
            for draw in range(number_of_balls):
                rand_ball = random.randint(0, (len(balls_left)-1))
                drawn_balls.append(balls_left[rand_ball])
                balls_left.pop(rand_ball)

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat = Hat(red=2, blue=5, green=3)
print(hat.contents)
print(hat.draw(4))
print(hat.contents)
