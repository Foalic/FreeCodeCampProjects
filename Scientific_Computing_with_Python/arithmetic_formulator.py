def arithmetic_arranger(problems, solved=False):
    import string

    arranged_problems = ""
    alphabet = string.ascii_letters

    strip_split_problems_list = []
    top_part = ""
    middle_part = ""
    bottom_line = ""
    answer_part = ""

    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        # Exception section
        for index,problem in enumerate(problems):

            if '*' in problem or '/' in problem:
                return "Error: Operator must be '+' or '-'."
            else:
                for part in problem.split():
                    if len(part) > 4:
                        return "Error: Numbers cannot be more than four digits."
                    else:
                        pass

            for letter in alphabet:
                if letter in problem:
                    return "Error: Numbers must only contain digits."
                else:
                    pass

          #Main arranging function for single problems
            if arranged_problems == "":
                #Preparing problem for arrangement
                split_problem = problem.split()
                strip_split_problem = []

                answer = str(eval(problem))

                for item in split_problem:
                    item = item.strip()
                    strip_split_problem.append(item)


                # Get largest digit
                if len(strip_split_problem[0]) > len(strip_split_problem[2]):
                    largest_digit_length = len(strip_split_problem[0])
                else:
                    largest_digit_length = len(strip_split_problem[2])

                # Arrange items for one problem
                if index == 0:
                    strip_split_problem[0] = (" " * 2) + (" " * (largest_digit_length - len(strip_split_problem[0]))) + strip_split_problem[0]
                    strip_split_problem[1] = strip_split_problem[1] + " " + (" " * (largest_digit_length - len(strip_split_problem[2]))) + strip_split_problem[2]
                    strip_split_problem[2] = ("-" * (largest_digit_length + 2))
                    if solved == True:
                        if len(answer) > largest_digit_length:
                            answer_line = (" " * (5 - len(answer))) + answer
                        else:
                            answer_line = (" " * ((largest_digit_length + 1) - len(answer))) + answer
                else:
                    strip_split_problem[0] = (" " * 6) + (" " * (largest_digit_length - len(strip_split_problem[0]))) + strip_split_problem[0]
                    strip_split_problem[1] = (" " * 4) + strip_split_problem[1] + " " + (" " * (largest_digit_length - len(strip_split_problem[2]))) + strip_split_problem[2]
                    strip_split_problem[2] = (" " * 4) + ("-" * (largest_digit_length + 2))
                    if solved == True:
                        if len(answer) > largest_digit_length:
                            answer_line = (" " * 5) + (" " * (5 - len(answer))) + answer
                        else:
                            answer_line = (" " * 5) + (" " * ((largest_digit_length + 1) - len(answer))) + answer


                # Add newlines to the end of the last problem
                if (index + 1) == len(problems):
                    strip_split_problem[0] = strip_split_problem[0] + "\n"
                    strip_split_problem[1] = strip_split_problem[1] + "\n"
                    strip_split_problem[2] = strip_split_problem[2]

                if solved == True:
                    strip_split_problem.append(answer_line)

                strip_split_problems_list.append(strip_split_problem)

            else:
                break


    # Bring all the problems parts together
    for problem in strip_split_problems_list:
        top_part = top_part + problem[0]
        middle_part = middle_part + problem[1]
        bottom_line = bottom_line + problem[2]
        if solved == True:
            answer_part = answer_part + problem[3]

    arranged_problems = top_part + middle_part + bottom_line
    if solved == True:
        arranged_problems = arranged_problems + "\n" + answer_part
    arranged_problems = "".join(arranged_problems)
    return arranged_problems
