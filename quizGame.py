# print("Welcome to the quiz game..")

# playing = input("Do you want to play? ")
# if  playing.lower() != "yes":
#     quit()
    
# print("okay! Let's start :) ")
# score = 0   
# # question   
# answer = input("What is the capital of France? ")

# if answer.lower() == "paris"  :
#     print("Correct! The capital of France is Paris.")
#     score +=1
# else:
#     print("Incorrect, the correct answer is Paris.")
    
# print( score) 
    
print("Welcome to the quiz game..")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's start :) ")
score = 0

# Questions and answers
questions = [
    ("What is the capital of France?", "paris"),
    ("What is the largest mammal?", "blue whale"),
    ("How many continents are there?", "seven"),
    ("What is the chemical symbol for water?", "h2o"),
    ("Who wrote 'Romeo and Juliet'?", "shakespeare"),
    ("What is the tallest mountain in the world?", "mount everest"),
    ("Which planet is known as the Red Planet?", "mars"),
    ("What is the main ingredient in guacamole?", "avocado"),
    ("What is the currency of Japan?", "yen"),
    ("What is the powerhouse of the cell?", "mitochondria")
]

# Asking questions
total_questions = len(questions)
for question, correct_answer in questions:
    answer = input(question + " ")
    if answer.lower() == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", correct_answer)

percentage_score = (score / total_questions) * 100
print("Your final score is:", score)
print("Your percentage score is:", "{:.2f}%".format(percentage_score))
