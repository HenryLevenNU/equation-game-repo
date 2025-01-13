import random
import operator as op

import numpy as np


def random_values(game_difficulty):
    """Chooses random values in range to be used in the generated equation.

    Parameters:
    game_difficulty (str): Influences the maximum integer of random numbers

    Returns:
    integer_1 (integer): The first non-algebraic number in the equation
    integer_2 (integer): The second non-algebraic number in the equation
    """
    max_value = difficulty_values(game_difficulty)
    integer_1 = random.randint(1, max_value)
    integer_2 = random.randint(1, max_value)
    return integer_1, integer_2


def difficulty_values(game_difficulty):
    """
    Sets constants for the upper limit 'random values' according to difficulty.

    Parameters:
    game_difficulty (str): Influences the maximum integer of random numbers

    Returns:
    max_value (int): Maximum of randomised number range based on difficulty.
    """
    if (game_difficulty == "Hard") or (game_difficulty == "2"):
        # Equation values will not exceed 12 for 'Hard', and '8' for 'Normal'.
        max_value = 14
    else:
        max_value = 8
    return max_value


def random_operator():
    """
    Sets a random operator out of 4 options to be used in the equation.

    Returns:
    operator_string (numpy.str): Selects a random operator in array.
    operator_converter (dict): Finds inverse operator for use as function.
    """
    # 4 options for equation operators listed in the array below.
    operator_array = np.array(["+", "-", "*", "/"])
    operator_string = operator_array[random.randint(0, 3)]

    # Converts to the inverse operator using a lookup table.
    operator_converter = {"+": op.sub, "-": op.add,
    "*": op.truediv, "/": op.mul}
    return operator_string, operator_converter


def get_user_input():
    """
    Asks user for their answer to the equation for each round.

    Returns:
    rounded_input (float): User's input answer rounded to 1 decimal place.
    """
    # The local variable, game_round, prints round number.
    user_input = input("   ⬆" + " What is the solution of 𝑥 in the equation: ")
    rounded_input = round(float(user_input), 1)
    return rounded_input


# Concatenates the elements of the equation to print to user.
def print_equation(game_round, operator, equation_int_1, equation_int_2):
    """
    Concatenates and prints out the equation that needs solving.

    Parameters:
    game_round (int): Needed here to print round number for each question.
    operator (str): Prints out the operator symbol in the equation.
    equation_int_1 (int): The first non-algebraic value used in the equation.
    equation_int_2 (int): The second non-algebraic value used in the equation.
    """
    print(
        "\n"
        + str(game_round)
        + ". 𝑥 "
        + operator
        + " "
        + str(equation_int_1)
        + " = "
        + str(equation_int_2)
    )
