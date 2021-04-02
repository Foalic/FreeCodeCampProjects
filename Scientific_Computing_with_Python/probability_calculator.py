import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for ball_colour,value in kwargs.items():
            for count in range(value):
                self.contents.append(ball_colour)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat = Hat(red=0)
print(hat.contents)
