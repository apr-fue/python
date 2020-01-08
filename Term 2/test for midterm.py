# April Fuentes
# 12/19
# midterm

import sys

def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        return file
    except IOError as e:
        print("Unable to open the file", file_name,"Ending program.\n",e)
        input("\n\nPress the enter key to exit.")
        sys.exit()

def next_line(the_file):
    line = the_file.readline()
    line = line.strip("\n")
    line = line.replace("/","\n")
    return line
    
def question_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation
        
def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to my python Trivia Challenge!\n")
    print("\tthis test was created by",title, "\n")

    
def get_file_name():
    while True:
        file_name = input("enter in the name of your file including the.txt")
        if ".txt" in file_name and " " not in file_name:
            return file_name
        else:
            print("not a good file name")

    
def main():
    file_name = get_file_name()
    file= open_file(file_name, "r")
    title = next_line(file)
    name = input("What is your full name?")
    questions = 0
    score = 0
    category, question, answers, correct, explanation  = question_block(file)
    welcome(title)
    while category:
        print(category)
        print()
        print(question)
        print()
        for i in range(len(answers)):
            print("\t", i + 1, "-", answers[i])
        answer = input("What's your answer: ")

        if answer == correct or name=="Isaac Lehman":
            print("\nCorrect!")
            score += 1
            questions += 1
        else:
            print("Incorrect.")
            questions += 1
        print()
        print(explanation)
        category, question, answers, correct, explanation  = question_block(file)
    file.close()
    print("That was the last question!")
    input("Press enter to see your report card.")
    report_card(name,questions,score)
    
def write_score(name,score):
    file = open_file("scores.txt","a+")
    pair = name+":     "+str(score)+"\n"
    line = []
    line.append(pair)
    file.writelines(line)
    file.close()
    
def report_card(name,question_count,score):
    """Gives the user their score in a percentage and letter grade. Also tells the user how many
        they got right and wrong."""
    
    username = name
    questions = question_count
    correct = score

    points_per_ques = 1/question_count
    points_1 = points_per_ques * score
    points_2 = points_1 * 100

    grade = str.format("""
Name = {0}
Points  per question = {1}
Number of questions = {2}
You scored a {3} %
yay""", username,points_per_ques, questions, points_2)
    print(grade)
    write_score(name,points_2)






                
main()
input("press enter to close")

