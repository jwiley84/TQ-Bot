from Question_reader import Question_reader
from brute_quiz import Quiz_Bot_Brute


quizexcel = "QuizBot.xlsx"
quiz_file = Question_reader(quizexcel).read_questions_from_file()
print(quiz_file)

quiz_length = len(quiz_file)
quiz_start = Quiz_Bot_Brute()
quiz_start.read_questions(quiz_file, quiz_length)


#TODO: Change to connect to Twitch, look for answers from users