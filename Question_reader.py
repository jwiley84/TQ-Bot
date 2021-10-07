import pandas as pd

class Question_reader():

    def __init__(self, file):
        self.file = file

    def read_questions_from_file(self):
        file = self.file
        data = pd.read_excel(file, usecols="A,B")
        qa_pairs = list(zip(data['Questions'], data['Answers']))
        return qa_pairs


# quizfile = "QuizBot.xlsx"

# x = Question_reader(quizfile)
# x.read_questions_from_file()