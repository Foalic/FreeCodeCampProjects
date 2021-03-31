import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        if len(kwargs) == 0:
            raise ValueError("Missing arguments: please enter at least one ball colour and an amount above 1 in format 'red=1'.")
        for ball_colour,value in kwargs.items():
            if value == 0 and len(kwargs) == 1:
                raise ValueError("Missing arguments: please enter at least one ball colour and an amount above 1 in format 'red=1'.")
            for count in range(value):
                self.contents.append(ball_colour)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat = Hat(red=0)
print(hat.contents)
