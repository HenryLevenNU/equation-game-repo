#  Equation Game Documentation

## 1.  User Guide

### 1.1  Overview

The Equation Game is an exciting game where you can prove your mathematical prowess. Regurgitate your High School algebra knowledge by solving each equation that gets sent your way! Watch out though... your score gets added up and displayed to you at the end. 

### 1.2  Features

Unique numbers and operator for each equation! After all, you don't want to see the same old equation each time, do you?

Choose how many rounds YOU want to play! Your wish is my command. 

Choose your difficulty level! Are you feeling sensible, or are you feeling brave enough to conquor the world?

### 1.3  Setup

***Prerequisites***

• You will need Python 3.7 (or later versions) to run the game.

• You can download Python by clicking [here](https://www.python.org/downloads/)

***Install the game***

• Visit my [Github page here](https://github.com/HenryLevenNU/equation-game-repo)

• Click the green button called ‘<> Code’ 

• In the drop-down menu that appears, click ‘Download ZIP’

• This will start downloading the ZIP folder to your device

• Open your Downloads folder in 'Finder' (File Explorer for Windows)

• Unzip it so it becomes a regular folder (by double clicking it on Mac)

• Right click -> Get info -> and copy the folder directory 

***Run the Game***

*Navigate to the 'Terminal' on Mac (or Command Prompt on Windows).
*Write 'cd ' and then paste in the folder directory like this:
```
cd /Users/your_name/Downloads/equation-game-repo-main
```
*Finally, start the game by typing:
```python main.py``` to run the game

### 1.4  Game Instructions

Once you start the game using the above instructions, simply follow the on-screen instructions.

It will first ask you to choose the Settings by which the game will be determined. Remember to input a number 'e.g 5' for number of rounds

Also, ensure you type 'Normal' or 'Hard' (not caps sensitive), or alternatively, 1 or 2 for these respectively.

Round 1 will then start, and you will need to work out the value of 𝑥 by using algebraic principles. Learn more about solving simple algebraic equations [here](https://www.cliffsnotes.com/study-guides/basic-math/basic-math-and-pre-algebra/variables-algebraic-expressions-and-simple-equations/solving-simple-equations):


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
In fact, the code clarifies the question and repeats the question for input until successful.

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

Additionally, I used pure functions; included docstrings and comments; and structured it in a modular, easy-to-interpret fashion. This makes the code easier to maintain.

***Score***

In the brief, the game needed to keep a score across multiple rounds. A global variable 'score' was created for this, which was used as a parameter and then returned from each function.
A function was used for increasing the score, and for no change to the score, to modularise this code and call one of them for each round. 

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

In the example below, an ‘array’ of 4 string operators (+, -, * and /) is created.

One of these operators is chosen, and corresponds to a random number between 1-4 which determines which position of the array is selected. This selected string is later used in the printed equation.

Meanwhile, the string needs to be converted into a more usable function. The ‘operator’ library that I used is a functional interface to give me more control to the standard operators. However, there is an extra layer of complexity as the operator function needs to be the opposite to the printed operator, due to the positioning of the equation elements. 

E.g.
x / 5 = 10
To solve for x: x = 10 * 5. 

```
def random_operator():
    operator_array = np.array(["+", "-", "*", "/"])
    operator_string = operator_array[random.randint(0, 3)]
    operator_converter = {"+": op.sub, "-": op.add,
    "*": op.truediv, "/": op.mul}
    return operator_string, operator_converter
```

### 2.4  Minimal Viable Product (MVP) - Conclusion
Considering the time constraints (Estimated: 15 hours programming and 5 hours training), I decided early-on to use a CLI to run the code rather than a GUI. The client brief allowed for both. I also decided to offer some customisability in settings (though limited). 

This can be iterated on the MVP – and next steps could include using more operators and allowing for negative values in Hard mode. 

However, the code is designed in a modular way to make changes easy to implement. Given more time, the project could be moved to a GUI to build on the user-centred design (UCD) of my functional and non-functional requirements.



