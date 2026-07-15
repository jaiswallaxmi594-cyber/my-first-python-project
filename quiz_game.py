print("Welcome to Python Quiz Game")

score = 0

questions = [
    {
        "question": "Who created Python?",
        "options": [
            "A. Dennis Ritchie",
            "B. Guido van Rossum",
            "C. James Gosling",
            "D. Elon Musk"
        ],
        "answer": "B"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": [
            "A. .java",
            "B. .html",
            "C. .py",
            "D. .cpp"
        ],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": [
            "A. print()",
            "B. input()",
            "C. output()",
            "D. show()"
        ],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "A. function",
            "B. define",
            "C. def",
            "D. fun"
        ],
        "answer": "C"
    },
    {
        "question": "Which data type is used to store True or False values?",
        "options": [
            "A. int",
            "B. bool",
            "C. str",
            "D. float"
        ],
        "answer": "B"
    }
]

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")

print("\nQuiz Completed!")
print("Your Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! You got all answers correct.")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")