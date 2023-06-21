from question import Question

questions_prompts = [
    "What color is an apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color is a banana?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color is a strawberry?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "c"),
    Question(questions_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.m_prompt)
        if answer == question.m_answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)