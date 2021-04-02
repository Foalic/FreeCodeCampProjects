import copy
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




def make_drawn_balls_list_to_dictionary(drawn_balls):
    drawn_balls_dict = dict()

    for ball in drawn_balls:
        if ball not in drawn_balls_dict:
            drawn_balls_dict[ball] = 1
        else:
            drawn_balls_dict[ball] += 1

    return drawn_balls_dict


def get_number_of_matched_experiments(hat, expected_balls, num_balls_drawn):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    balls_matched = 0
    is_match = False

    drawn_balls_dict = make_drawn_balls_list_to_dictionary(drawn_balls)

    for key_expected,value_expected in expected_balls.items():
        for key_drawn,value_drawn in drawn_balls_dict.items():
            if key_expected == key_drawn:
                if value_drawn >= value_expected:
                    ball_matches = True
                    break
                else:
                    continue
        else:
            continue

        if ball_matches:
            balls_matched += 1

    if balls_matched == len(expected_balls):
        is_match = True

    return is_match



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matched_experiments = 0

    for experiment in range(num_experiments):
        is_match = get_number_of_matched_experiments(hat, expected_balls, num_balls_drawn)
        if is_match:
            matched_experiments += 1

    probability = matched_experiments / num_experiments
    return probability
