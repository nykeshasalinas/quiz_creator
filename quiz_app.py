# Import tkinter library for application's GUI
# Import random module to randomize questions

import tkinter as tk
import random

# Read questions in quiz_created.txt
class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer.lower()

def load_questions_from_file(filename):
    questions = []
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            for i in range(0, len(lines), 6):
                if i + 5 < len(lines):
                    q_text = lines[i]
                    options = lines[i+1:i+5]
                    answer_line = lines[i+5].lower()

                    if "correct answer:" in answer_line:
                        answer = answer_line.split("correct answer:")[1].strip().split('.')[0].lower()
                        questions.append(Question(q_text, options, answer))
                    else:
                        print(f"Warning: Malformed answer line for question: {q_text}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return questions

if __name__ == "__main__":
    question_list = load_questions_from_file("quiz_created.txt")
    for q in question_list:
        print(f"Q: {q.text}")
        for opt in q.options:
            print(f"   {opt}")
        print(f"Answer: {q.answer}")
        print()

# Make the the app's GUI using tkinter library

# Generate the questions randomly and allow the user to answer
# Check if the user's answer is correct
# Generate the user's score