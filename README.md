![image](https://github.com/user-attachments/assets/d3bed474-f1f6-4801-8221-cd009fa015ca)![image](https://github.com/user-attachments/assets/73a61efe-cc08-4e4b-b6dd-33efa37b7357)#  Equation Game Documentation

###  Executive Summary

## 1.  User Guide

### 1.1  Setup

### 1.2  Game Instructions



## 2.  Technical Documentation

### 2.1  Solution Architecture

![image](https://github.com/user-attachments/assets/2eb7bebd-41a8-4389-99c7-535273853ede)

The architecture broke down into three overarching blocks to maximise modularity:

•	The introduction and Settings page

•	The equation generation based on prior Settings

•	The answer checking and subsequent effect on score

•	The ‘main’ gameplay which structures the previous 3 aspects.

### 2.2  Non-Functional Requirements

***Usability***

As seen in the solution architecture diagram above, the system uses handles incorrect inputs for 'Settings' and 'User input', for example in the case of incorrect data types like string, instead of their int/float answer.
In fact, the code clarifies the question and repeats the question for input until they are successful. This can be seen in the following example:

```
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
```
***Reliability***

Command Line Interfaces are performant, so the Python program should run instantly. 
Rigorous testing was carried out during and after development to ensure that all known bugs were fixed. 

***Scalability***

The code will be run locally. Additionally, it was programmed in a modular way, which allows for more functionality to be added down the line. 


### 2.3  Functional Requirements

***Answer Verification***

When the user enters an answer, the system successfully accepts both integer and float data types. 
It proceeds to verify whether the answer is correct through the below code, where solution and user_input are rounded to 1 d.p and compared.
```
    if round(solution, 1) == round(user_input, 1):
        print("Your answer of '" + str(user_input) + "' is correct!")
        # Prints the score at the end of each round.
        score = increase_score(current_round, number_of_rounds, score)
```
***PEP8***

Development followed PEP8 Guidelines which was aided by using the ‘Black’ VSCode Extension, though I had to manually change some of the lines of code to fall within PEP’s 79 characters advised line limit. 
Moving forward, I recommend a developer using ‘AutoPep-8’ extension instead as it has greater control over this.

***Score***

In the brief, the game needed to keep a score across multiple rounds. A global variable 'score' was created for this, which was used as a parameter and then returned from each function.
A function was used for increasing the score, and for no change to the score, to modularise this code and call one of them for each round. 

***Maintainability***

And wrapping it all up, I used pure functions; included docstrings and comments; and structured it in a modular, easy-to-interpret fashion. 
This makes the code easier to maintain and will allow more functionality to be added down the line as the MVP gets iterated on. 
```
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
```

### 2.4 Unique Selling Points
***Difficulty Levels***
The game also needs to accommodate a range of users. Therefore, the game was designed with different difficulty levels for varying mathematical skill levels of users in mind. 
To do this, 'max_value' takes either 14 for Hard mode, or 8 for Normal mode. To improve this further, '1' in the following example can be replaced by a var, min_value which could be in the negatives for Hard mode.
```
    max_value = difficulty_values(game_difficulty)
    integer_1 = random.randint(1, max_value)
    integer_2 = random.randint(1, max_value)
```

***Unique Operator each Round***

In the example below, an ‘array’ of 4 different string operators is established. These include +, -, * and /. 

One of these operators is then chosen, with a random number between 1-4 being generated and corresponding to which position of the array is selected to be used. This selected string is later used in the equation that is printed to the user. 

Meanwhile, in the back end, the string needs to be converted into a more usable function. The ‘operator’ library that I used is a functional interface to give me more control to the standard operators. However, there is an extra layer of complexity as the operator function needs to be the opposite to the printed operator, due to the positioning of the equation elements. 

E.g.
x / 5 = 10
To solve for x: x = 10 * 5. 

```
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
```

### 2.4  Minimal Viable Product (MVP) - Conclusion
Considering the time constraints and need for accelerating development (I estimated I only had 15 hours programming and 5 hours training time), I decided early-on to use a CLI to run the code rather than a GUI. The client brief allowed for both. I also decided to offer some customisability in settings (though limited). This can be iterated on the MVP – and next steps could include using more operators and allowing for negative values in Hard mode. 

However, the code is designed in a modular way to make these changes easy to implement. Given more time, the project could be moved to a GUI to build on the user-centred design (UCD) of my functional and non-functional requirements.



