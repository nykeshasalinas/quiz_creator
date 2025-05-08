# Program a quiz creator
text_file = open("quiz_created.txt", "w")
print("WELCOME TO THE QUIZ CREATOR!")
question_count = 1

# Create a loop that asks user to input question
while True:
    question = input(f"Input Quiz Question {question_count}: ")
    text_file.write(f"{question}\n")
    question_count += 1
   
    # Ask user to input options a, b, c, and d
    print("Input Options: ")
    option_a = input("a. ")
    text_file.write(f"a. {option_a}\n")
    option_b = input("b. ")
    text_file.write(f"b. {option_b}\n")
    option_c = input("c. ")
    text_file.write(f"c. {option_c}\n")
    option_d = input("d. ")
    text_file.write(f"d. {option_d}\n")

    # Ask user to input the correct answer among the options
    correct_answer = input("Correct Answer (a/b/c/d): ")
    if correct_answer.lower() == "a":
        text_file.write(f"Correct Answer: a. {option_a}\n")
    elif correct_answer.lower() == "b":
        text_file.write(f"Correct Answer: b. {option_b}\n")
    elif correct_answer.lower() == "c":
        text_file.write(f"Correct Answer: c. {option_c}\n")
    elif correct_answer.lower() == "d":
        text_file.write(f"Correct Answer: d. {option_d}\n")

    # Import user inputs to text file

    # Ask the user if they want to add question
    add_question = input("Add another question (Yes/No)? ")
    if add_question.capitalize() == "Yes":
        # Go back to loop if Yes
        print("----------------------------------------------------------------------------------------------------")
        continue
    else:
        print("----------------------------------------------------------------------------------------------------")
        print("WORK SAVED")
        exit()
        # Else, exit the program

    # Save the quiz in the text file