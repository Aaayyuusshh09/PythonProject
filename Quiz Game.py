"""
Quiz Game
Covers: input, variables, data types, if-else, loops, functions, dicts,
lists, nesting, random, scope, global vars/constants, docstrings
"""

import random

# ---- Global Constant ----
MAX_QUESTIONS = 5

# ---- Question Bank (list of dictionaries) ----
questions = [
    {"question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
     "answer": "Delhi"},
    {"question": "Which keyword is used to define a function in Python?",
     "options": ["func", "def", "function", "lambda"], "answer": "def"},
    {"question": "What does RAM stand for?",
     "options": ["Read Access Memory", "Random Access Memory", "Rapid Access Memory", "Run Access Memory"],
     "answer": "Random Access Memory"},
    {"question": "Which data type is immutable in Python?", "options": ["List", "Set", "Tuple", "Dictionary"],
     "answer": "Tuple"},
    {"question": "What is 5 ** 2 in Python?", "options": ["10", "25", "7", "None"], "answer": "25"},
    {"question": "Who developed Python?",
     "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
     "answer": "Guido van Rossum"},
]


# ---- Function to Ask Question ----
def ask_question(q):
    """Ask a single question and return if user got it right"""
    print("\n" + q["question"])

    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")

    try:
        choice = int(input("Enter option number: "))
        if q["options"][choice - 1] == q["answer"]:
            print("✅ Correct!")
            return True
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
            return False
    except (ValueError, IndexError):
        print("⚠️ Invalid input, counted as wrong.")
        return False


# ---- Main Game Function ----
def play_quiz():
    """Play the quiz game"""
    print("🎮 Welcome to the Quiz Game 🎮")
    name = input("Enter your name: ")

    score = 0
    # Pick random questions
    selected = random.sample(questions, MAX_QUESTIONS)

    for q in selected:
        if ask_question(q):
            score += 1

    print(f"\n🏆 {name}, your final score is {score}/{MAX_QUESTIONS}")

    # Show grade
    if score == MAX_QUESTIONS:
        print("🎉 Excellent! Full Score!")
    elif score >= 3:
        print("👍 Good Job!")
    else:
        print("📚 Keep practicing!")


# ---- Run Game ----
play_quiz()
