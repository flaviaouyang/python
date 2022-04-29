# Project: Generating Random Quiz Files
import os
import random

# check cwd
# print(os.getcwd())
os.chdir('/Users/flaviaouyang/AutomatePython/source_code/generate_random_quiz_file')
# print(os.getcwd())

questions = {
    'initialize a repository': 'git init',
    'clone an existing repository': 'git clone url',
    'check the status of your files': 'git status',
    'add files to statging area': 'git add',
    'commit added files': 'git commit'
}

for i in range(5):
    # create 10 files, 5 for quiz files, 5 for answers files
    quiz_file = open('quiz' + str(i + 1) + '.txt', 'w')
    answer_file = open('answer' + str(i + 1) + '.txt', 'w')

    # write headers for quiz files and answer files
    quiz_file.write("Git Basics Quiz" + str(i + 1) + "\n\n\n")
    answer_file.write('Answer key for quiz' + str(i + 1) + "\n\n\n")

    # put questions in to a list
    # write questions and answers
    questions_list = list(questions.keys())
    random.shuffle(questions_list)
    for j in range(len(questions_list)):
        quiz_file.write('Question ' + str(j + 1) +
                        ': ' + questions_list[j] + "\n")
        answer_file.write('Answer for question ' + str(j + 1) +
                          ': ' + questions.get(questions_list[j], 'ERROR') + "\n")

    # close both files
    quiz_file.close()
    answer_file.close()
