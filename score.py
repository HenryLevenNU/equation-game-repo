from generate_equation import *


def verify_answer(current_round, number_of_rounds,
    score, solution, user_input):
    """
    Verifies user input against solution, and returns updated score.

    Parameters:
    current_round (integer): The current round being played out.
    number_of_rounds (integer): The total number of rounds to be played.
    score (integer): The current score of the game from all rounds.
    solution (float): The correct answer of that particular round.
    user_input (float): The user's answer of that particular round.

    Returns:
    score (integer): The updated score (either +1 or unchanged)
    """
    # Verifies user input matches the calculated solution to 1 d.p
    if round(solution, 1) == round(user_input, 1):
        print("Your answer of '" + str(user_input) + "' is correct!")
        # Prints the score at the end of each round.
        score = increase_score(current_round, number_of_rounds, score)
    else:
        # Prints message comparing user input with the actual solution.
        print_when_incorrect(user_input, solution)
        # User is informed that there is no change to the score.
        score = same_score(current_round, number_of_rounds, score)
    return score


def print_when_incorrect(user_input, solution):
    """
    Informs user that their answer is incorrect, and prints the answer

    Parameters:
    user_input (float): The user's answer to the equation of that round.
    solution (float): The calculated solution of that particular round.
    """
    print(
        "Unfortunately, your answer of '"
        + str(user_input)
        + "' was wrong. The answer is "
        + str(solution)
        + "."
    )


def same_score(current_round, number_of_rounds, score):
    """
    Informs user there is no change to score, except during last round

    Parameters:
    current_round (integer): The current round being played out.
    number_of_rounds (integer): The total number of rounds to be played.
    score (integer): The current score of the game.

    Returns:
    score (integer): Though unchanged, the score is fed back to main.py
    """
    # Last iteration is not printed. Final score is revealed at end.
    if current_round < number_of_rounds:
        print("\nYour score remains: " + str(score))
    return score


def increase_score(current_round, number_of_rounds, score):
    """
    Takes score and increases by 1, except during last round.

    Parameters:
    current_round (int): The current round being played out.
    number_of_roudns (int): The total number of rounds to be played.
    score (int): The current score of the game

    Returns
    score (int): The updated score (added 1) when correct answer.
    """
    score += 1
    if current_round < number_of_rounds:
        print("\nYour score is now: " + str(score))
    return score


def final_score(score, number_of_rounds):
    """
    Prints the final score out of total rounds and closing sequence.

    Parameters:
    score (int): The final score after all the rounds have been played
    number_of_rounds (int): Number of rounds played in entirety.
    """
    print(
        "\nI can now conclude that your final score is... "
        + str(score)
        + " out of "
        + str(number_of_rounds)
    )
    print("\nWell played! \nThanks for playing my maths game.")
