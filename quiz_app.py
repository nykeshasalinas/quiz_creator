# Import tkinter library for application's GUI
# Import random module to randomize questions
# Read questions in quiz_created.txt
# Generate the questions randomly and allow the user to answer
# Check if the user's answer is correct
# Generate the user's score

import tkinter as tk
import random

with open('quiz_created.txt', 'r') as file:
    content = file.readlines()[0:5]
    print(content)