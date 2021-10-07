import random
from Question_reader import Question_reader

class Quiz_Bot_Brute:
    
    def continue_prompt():
        print("Would you like to continue, y or n?")
        answer = input().lower()
        if answer == 'y'  or answer == 'yes':
            print("ok, next question!")
            return True
        else:
            print("ok, goodbye!")
            return False


    def read_questions(self, questions, num_questions):
        question_set = []
        total = num_questions

        while total > 0:
            random_num = random.randint(0, len(questions) - 1)
            if random_num not in question_set:
                question_set.append(random_num)
            else:
                continue
            total -= 1

        for index in range(len(question_set)):
            print(index)
            print(questions[question_set[index]][0])
            
            answer = input().lower()
            if answer == (questions[question_set[index]][1]).lower():
                print("Good job!")
            else:
                print("Nope!")
            if index < len(question_set) - 1:
                if self.continue_prompt() == True:
                    continue
                else:
                    break
            else:
                print("that's all folks!")
            



move_to_file = [("What is two plus two", "Four"), ("Why is this show hokey?", "Overacting"), ("What is the answer to life, the universe, everything?", "Four-Two"), ("QFour", "Four"), ("QFive", "Five"), ("QSix", "Six")]

quizexcel = "QuizBot.xlsx"
quiz_file = Question_reader(quizexcel)
#test = Question_reader.read_questions_from_file(self, quizexcel)

#read_questions(move_to_file, 4)
quiz_file.read_questions_from_file()