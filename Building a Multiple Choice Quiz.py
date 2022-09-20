# multiple choice quiz
# Fomulario de multipla escolha
from Question import Question

question_prompts = [
    "What color are apples?\n(a) Read/Green\n(b) Purple\n(c) Orange\n\n",
     "What color are Bananas?\n(a) Teal\n(b) Margenta\n(c) Yellow\n\n",
     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "B")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)