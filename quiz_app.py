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

        # Add color to the background
        self.master.config(bg="black")

        # Create start button before directing to the quiz
        self.start_button = tk.Button(self.master, text="Start Quiz", command=self.start_quiz, font=("Arial", 16), bg="black", fg="white")
        self.start_button.pack(pady=20, padx=20, expand=True)

        # Create frame for question
        self.question_frame = tk.Frame(self.master, bd=3, relief="solid", padx=10, pady=5, bg="black", highlightbackground="blue", highlightthickness=2)

        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 18), wraplength=400, justify="left", fg="white", bg="black")
        self.question_label.pack(padx=20, pady=10)
        
        # Create buttons for options
        self.radio_buttons = []
        for _ in range(4):
            rb = tk.Radiobutton(self.master, text="", variable=self.selected_answer, value="", font=("Arial", 14), bg="black", fg="white", selectcolor="black")
            self.radio_buttons.append(rb)

        # Create submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer, font=("Arial", 16), bg="black", fg="white")

    # Create start button
    def start_quiz(self):
        self.start_button.pack_forget()
        self.question_frame.pack(pady=20, padx=20)
        for rb in self.radio_buttons:
            rb.pack(anchor="w", padx=20, pady=10)
        self.submit_button.pack(pady=20)
        self.display_question()
        
    # Design how questions will displayed
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
                    if "correct answer:" in answer_line:
                        answer = answer_line.split("correct answer:")[1].strip().split('.')[0].lower()
                        questions.append(Question(q_text, options, answer))
                    else:
                        print(f"Warning: Malformed answer line at question: {q_text}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return questions

# Add a funtion to center the GUI
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    center_window(root, 600, 500)  # Center the window on the screen
    question_list = load_questions_from_file("quiz_created.txt")
    if question_list:
        random.shuffle(question_list) # Generate the questions randomly and allow the user to answer
        app = QuizApp(root, question_list)
        root.mainloop()
    else:
        print("No questions found in the file.")