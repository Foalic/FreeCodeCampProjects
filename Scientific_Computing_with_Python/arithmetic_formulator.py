import string

def arithmetic_arranger(problems, solved=False):
    list_of_arranged_problems = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for index,problem in enumerate(problems):

        # Exception section
        input_error = check_for_invalid_input(problem)
        if input_error != None:
            return input_error

      #Main arranging function for single problems
        list_of_arranged_problems = get_list_of_arranged_problems(problems, solved, index, problem, list_of_arranged_problems)

    # Bring all the problems parts together
    arranged_problems, answer_line = arrange_problems_with_eachother(solved, list_of_arranged_problems)

    if solved == True:
        arranged_problems = arranged_problems + "\n" + answer_line

    arranged_problems = "".join(arranged_problems)

    return arranged_problems





def check_for_invalid_input(problem):
    alphabet = string.ascii_letters

    if '*' in problem or '/' in problem:
        return "Error: Operator must be '+' or '-'."

    for part in problem.split():
        if len(part) > 4:
            return "Error: Numbers cannot be more than four digits."

    for letter in alphabet:
        if letter in problem:
            return "Error: Numbers must only contain digits."




#Preparing problem for arrangement
def get_list_of_items_in_problem(problem):
    split_problem = problem.split()
    strip_split_problem = []

    for item in split_problem:
        item = item.strip()
        strip_split_problem.append(item)

    return strip_split_problem




def get_length_of_largest_digit(strip_split_problem):
    if len(strip_split_problem[0]) > len(strip_split_problem[2]):
        return len(strip_split_problem[0])
    else:
        return len(strip_split_problem[2])




# Arrange items for one problem
def arrange_one_problems_items(problems, index, strip_split_problem, length_of_largest_digit):
    strip_split_problem[0] = (" " * 2) + (" " * (length_of_largest_digit - len(strip_split_problem[0]))) + strip_split_problem[0]
    strip_split_problem[1] = strip_split_problem[1] + " " + (" " * (length_of_largest_digit - len(strip_split_problem[2]))) + strip_split_problem[2]
    strip_split_problem[2] = ("-" * (length_of_largest_digit + 2))
    if index != 0:
        strip_split_problem[0] = (" " * 4) + strip_split_problem[0]
        strip_split_problem[1] = (" " * 4) + strip_split_problem[1]
        strip_split_problem[2] = (" " * 4) + strip_split_problem[2]
    if (index + 1) == len(problems):
        strip_split_problem[0] = strip_split_problem[0] + "\n"
        strip_split_problem[1] = strip_split_problem[1] + "\n"

    return strip_split_problem




def arrange_one_problems_answer(index, answer, length_of_largest_digit):
    if len(answer) > length_of_largest_digit:
        answer_arranged = (" " * (5 - len(answer))) + answer
    else:
        answer_arranged = (" " * ((length_of_largest_digit + 1) - len(answer))) + answer
    if index != 0:
        answer_arranged = (" " * 5) + answer_arranged

    return answer_arranged



def get_list_of_arranged_problems(problems, solved, index, problem, list_of_arranged_problems):
    answer = str(eval(problem))

    strip_split_problem = get_list_of_items_in_problem(problem)

    length_of_largest_digit = get_length_of_largest_digit(strip_split_problem)

    strip_split_problem = arrange_one_problems_items(problems, index, strip_split_problem, length_of_largest_digit)
    if solved == True:
        answer_arranged = arrange_one_problems_answer(index, answer, length_of_largest_digit)
        strip_split_problem.append(answer_arranged)

    list_of_arranged_problems.append(strip_split_problem)

    return list_of_arranged_problems




def arrange_problems_with_eachother(solved, list_of_arranged_problems):
    top_line = ""
    middle_line = ""
    bottom_line = ""
    answer_line = ""

    for problem in list_of_arranged_problems:
        top_line = top_line + problem[0]
        middle_line = middle_line + problem[1]
        bottom_line = bottom_line + problem[2]
        if solved == True:
            answer_line = answer_line + problem[3]

    arranged_problems = top_line + middle_line + bottom_line

    return arranged_problems, answer_line
