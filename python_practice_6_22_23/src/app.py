from question import Question
from student import Student
from chef import Chef
from chineseChef import ChineseChef
questions_prompts = [
    "What color is an apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "\nWhat color is a banana?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "\nWhat color is a strawberry?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

question1 = Question(questions_prompts[0], "a")
question2 = Question(questions_prompts[1], "c")
question3 = Question(questions_prompts[2], "b")

questions = [
    question1, question2, question3 
]

student1 = Student("Gabriel", "Computer Engineering", 3.4, False)
chef = Chef()
chinese_chef = ChineseChef()

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.m_prompt)
        if answer == question.m_answer:
            score += 1
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct")


def main():
    #run_test(questions)
    #print(student1.on_honor_roll())
    chef.make_chicken()
    chef.make_salad()
    chef.make_special_dish()
    chinese_chef.make_special_dish()


if __name__ == "__main__":
    main()
