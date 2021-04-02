import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for ball_colour,value in kwargs.items():
            for count in range(value):
                self.contents.append(ball_colour)


    def draw(self, num_balls_drawn):
        drawn_balls = []

        if num_balls_drawn > len(self.contents):
            drawn_balls = self.contents
        else:
            for draw in range(num_balls_drawn):
                rand_ball = random.randint(0, (len(self.contents)-1))
                drawn_balls.append(self.contents[rand_ball])
                self.contents.pop(rand_ball)

        return drawn_balls



def get_number_of_matched_experiments(hat, expected_balls, num_balls_drawn):
    matched_experiments = 0
    drawn_balls = hat.draw(num_balls_drawn)
    drawn_balls_dict = dict()
    is_match = False

    for ball in drawn_balls:
        if ball not in drawn_balls_dict:
            drawn_balls_dict[ball] = 1
        else:
            drawn_balls_dict[ball] += 1

    for key_drawn,value_drawn in drawn_balls_dict.items():
        for key_expected,value_expected in expected_balls.items():
            if key_expected == key_drawn:
                if value_drawn >= value_expected:
                    is_match = True
                    break
                else:
                    continue
        else:
            continue

        if is_match:
            matched_experiments += 1

    return matched_experiments



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    balls_in_hat = [ball for ball in hat.contents]

    for experiment in range(num_experiments):
        matched_experiments= get_number_of_matched_experiments(hat, expected_balls, num_balls_drawn)

    probability = matched_experiments / num_experiments
    return probability

#
# hat = Hat(red=9, blue=10, green=30)
# print(hat.contents)
# print(hat.draw(4))
# print(hat.contents)
#
# print(experiment(hat, {"red":1, "blue":1, "green":1}, 20, 2000))
