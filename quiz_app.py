# Import tkinter library for application's GUI
# Import random module to randomize questions

import tkinter as tk
import random

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer.lower()

# Create question and answer screen
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
                    
                    # Check for "Answer:" or "Correct Answer:"
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
    question_list = load_questions_from_file("quiz_created.txt")  # Your text file name here
    if question_list:
        random.shuffle(question_list)  # 🔀 Shuffle questions
        app = QuizApp(root, question_list)
        root.mainloop()
    else:
        print("No questions found in the file.")

# Generate the questions randomly and allow the user to answer
# Check if the user's answer is correct
# Generate the user's score