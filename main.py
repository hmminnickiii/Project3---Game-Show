# REQUIREMENTS
# Display title of game show
# Display rules of game show
# Store 3+ T/F questions in a tuple
# Store answers in a tuple
# Loop through questions
# Get and validate user answers and store them
# Keep track of the number of correct answers
# Display the number of correct answers

# Display title of game show
print(r"""
 .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |  _______     | | |  _________   | | |      __      | | |  ________    | | |  ____  ____  | | |    ______    | |
| | |_   __ \    | | | |_   ___  |  | | |     /  \     | | | |_   ___ `.  | | | |_  _||_  _| | | |   / _ __ `.  | |
| |   | |__) |   | | |   | |_  \_|  | | |    / /\ \    | | |   | |   `. \ | | |   \ \  / /   | | |  |_/____) |  | |
| |   |  __ /    | | |   |  _|  _   | | |   / ____ \   | | |   | |    | | | | |    \ \/ /    | | |    /  ___.'  | |
| |  _| |  \ \_  | | |  _| |___/ |  | | | _/ /    \ \_ | | |  _| |___.' / | | |    _|  |_    | | |    |_|       | |
| | |____| |___| | | | |_________|  | | ||____|  |____|| | | |________.'  | | |   |______|   | | |    (_)       | |
| |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' 
""")

print("~ Welcome to Interrogation - A Game You May Not Want to Play ~")
print("                 **Muahhhhaaahhhhahhhh!**")
print()

# Display rules of game show
print("Interrogation is a quiz/game comprised of several different Yes/No questions. Please ONLY enter the letter T for true and F for false or you will be stuck here forever..... Enjoy!")
print()

# Store T/F questions in a tuple
questions = ("Q1. The Earth is a globe.", "Q2. Humans landed on the moon in 1968.", "Q3. The movie Independence Day is based on a true story.", "Q4. The movie Apollo 13 is based on a true story.")

# Store answers in a tuple
answers = ("T", "F", "F", "T")

# Variable to track correct answers
correctAnswerCount = 0

# Loop through questions,  and record answers, and update count of correct answers
numberOfQuestions = len(questions)

for index in range(numberOfQuestions):
  print(questions[index])
  answer = input("Please answer 'T' for true or 'F' for false: ")
 
  # Validate input format 
  while (answer != "T" and answer != "F"):
    print("Invalid answer. Please answer using ONLY 'T' for true or 'F' for false.")
    print()
    print(questions[index])
    answer = input("Please answer 'T' for true or 'F' for false: ")
  print()

  if (answer == answers[index]):
    correctAnswerCount += 1

# Display the number of correct answers
print(f"You got {correctAnswerCount} answer(s) correct!")
if (correctAnswerCount == 4):
  print("Perfect Score!")
elif (correctAnswerCount == 3):
  print("3/4 not too shabby.")
elif (correctAnswerCount == 2):
  print("You have some reading to do.")
elif (correctAnswerCount == 1):
  print("You have much more reading to do.")
else:
  print("History and science teachers have failed you or you are willfully answering incorrectly.")