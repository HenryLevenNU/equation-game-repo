from generate_equation import *
from score import *
from instructions import *

print("Welcome! Here to prove your mathematical prowess?")
# Initiates game settings
game_difficulty, number_of_rounds = settings()


def gameplay(number_of_rounds, game_difficulty):
    """
    Loops for each round of the game with a new equation shown each time.

    Parameters:
    number_of_rounds (integer): The total number of rounds to be played.
    game_difficulty (string): Selected game difficulty of Normal or Hard

    Raises:
    ValueError: If an invalid answer was input by user (such as a string).

    Returns:
    score (integer): The final, tallied up score of all the rounds.
    """
    # Sets initial score to 0.
    score = 0
    for index in range(1, number_of_rounds + 1, 1):
        integer_1, integer_2 = random_values(game_difficulty)
        operator_string, operator_converter = random_operator()

        # 'Try, except' verifies user input is not blank or invalid type.
        try:
            # Prints the equation and asks user to input their solution.
            print_equation(index, operator_string, integer_1, integer_2)
            user_input = get_user_input()

            # Calculates the exact answer to the equation.
            solution = float(operator_converter[operator_string]
            (integer_2, integer_1))

            # Verifies that the input answer matches the calculated solution.
            score = verify_answer(index, number_of_rounds,
            score, solution, user_input)
        except ValueError:
            print("You did not provide a suitable number.")
            print("Skipping this round!")
            # Score remains unchanged for wrong answer/incorrect data type.
            score = same_score(index, number_of_rounds, score)
    return score


score = gameplay(number_of_rounds, game_difficulty)
# Runs the final sequence, informing the user of the final score.
final_score(score, number_of_rounds)
