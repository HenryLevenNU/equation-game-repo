def settings():
    """
    Initiates user game settings with functions for difficulty and rounds.

    Returns:
    number_of_rounds (integer): How many rounds the user wishes to play.
    game_difficulty (string): Selected game difficulty (Normal or Hard)
    """
    print("Opening Settings...")
    number_of_rounds = select_rounds()
    game_difficulty = select_difficulty()
    # If game difficulty is hard, solutions may include decimals.
    if game_difficulty == "Hard":
        print("Answer to 1 d.p if your answer is not a whole number. Ready?")
    print("Let's get started...")
    return game_difficulty, number_of_rounds


def select_rounds():
    """
    Repeatedly asks user until they provide a valid integer for rounds.

    Returns:
    number_of_rounds (integer): How many rounds the user wishes to play.

    Raises:
    ValueError: If the input is a string or non-integer.
    """
    input_rounds_complete = False
    while input_rounds_complete == False:
        try:
            number_of_rounds = int(input("Enter a number of rounds to play: "))
            if number_of_rounds > 0:
                input_rounds_complete = True
        except ValueError:
            print("Invalid. Please enter a valid number.")
    return number_of_rounds


def select_difficulty():
    """
    Repeatedly asks user for what difficulty of the game they want.

    Returns:
    game_difficulty (integer): Difficulty level, Normal or Hard, of the game.

    Raises:
    ValueError: If user does not input one of the 4 accepted responses.
    """
    input_difficulty_complete = False
    while input_difficulty_complete == False:
        try:
            game_difficulty = input("Enter game difficulty: 'Normal'/'Hard' ")
            # .title() ensures answer is not caps sensitive.
            game_difficulty = game_difficulty.title()
            valid_difficulty = "Normal", "Hard", "1", "2"
            if game_difficulty in valid_difficulty:
                input_difficulty_complete = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid. Please enter '1' for Normal or '2' for Hard mode.")
    return game_difficulty
