questions = [
    {
        "prompt": "Which is the best anime of all time?",
        "options": ["A - One Piece", "B - Naruto", "C - Attack on Titans", "D - DragonBall Z"],
        "answer": "A"
    },
    {
        "prompt": "Which footballer is the greates of all time?",
        "options": ["A - CR7", "B - LM10", "C - Pele", "D - Maradona"],
        "answer": "B"
    },
    {
        "prompt": "Who is the best chess player of all time?",
        "options": ["A - Garry Kasparov", "B - Magnus Carlsen", "C - Bobby Fischer", "D - Jose Raul Capablanca"],
        "answer": "A"
    },
    {
        "prompt": "Best sport of all time?",
        "options": ["A - Chess", "B - Cricket", "C - Basketball", "D - Football"],
        "answer": "D"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter answer: ")
        if answer == question["answer"]:
            print("Correct! \n")
            score += 1
        else:
            print("Yo... wrong answer :/  Solution is: ",question["answer"],"\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)