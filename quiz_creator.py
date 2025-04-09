# Program a quiz creator
text_file = open("quiz_created.txt", "+w")

# Create a loop that asks user to input question
while True:
    question = input("Input Quiz Question: ")
    # Ask user to input options a, b, c, and d
    print("Input Options: ")
    option_a = input("a. ")
    option_b = input("b. ")
    option_c = input("c. ")
    option_d = input("d. ")

    # Ask user to input the correct answer among the options
    correct_answer = input("Correct Answer (a/b/c/d): ")

    # Import user inputs to text file

    # Ask the user if they want to add question
    add_question = input("Add another question (Yes/No)? ")
    if add_question == "Yes":
        # Go back to loop if Yes
        continue
    else:
        exit()
        # Else, exit the program
    # Save the quiz in the text file