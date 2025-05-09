# Import tkinter library for application's GUI
# Import random module to randomize questions

import tkinter as tk
from tkinter import messagebox
import random

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer.lower()

# Create question and answer screen
class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Quiz App")
        self.questions = questions
        self.current_q = 0
        self.score = 0
        self.selected_answer = tk.StringVar()

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        # Create buttons for options
        self.radio_buttons = []
        for _ in range(4):
            rb = tk.Radiobutton(self.master, text="", variable=self.selected_answer, value="", font=("Arial", 12))
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        # Create submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

    def display_question(self):
        question = self.questions[self.current_q]
        self.question_label.config(text=f"Q{self.current_q + 1}: {question.text}")
        self.selected_answer.set(None)
        for i, option in enumerate(question.options):
            value = option.split('.')[0].strip().lower()
            self.radio_buttons[i].config(text=option, value=value)

    # Generate the user's score
    def check_answer(self):
        user_answer = self.selected_answer.get()
        correct_answer = self.questions[self.current_q].answer
        if user_answer == correct_answer:
            self.score += 1

        self.current_q += 1
        if self.current_q < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("You Completed the Quiz!", f"Score: {self.score}/{len(self.questions)}")
            self.master.quit()

# Read questions in quiz_created.txt
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
                    
                    # Check if the user's answer is correct
                    if "answer:" in answer_line:
                        answer = answer_line.split("answer:")[1].strip()
                        questions.append(Question(q_text, options, answer))
                    elif "correct answer:" in answer_line:
                        answer = answer_line.split("correct answer:")[1].strip()
                        questions.append(Question(q_text, options, answer))
                    else:
                        print(f"Warning: Malformed answer line at question: {q_text}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return questions

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    question_list = load_questions_from_file("quiz_created.txt")
    if question_list:
        random.shuffle(question_list) # Generate the questions randomly and allow the user to answer
        app = QuizApp(root, question_list)
        root.mainloop()
    else:
        print("No questions found in the file.")