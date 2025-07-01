import data
class QuizBrain:
    def __init__(self):
        self.total_questions = len(data.question_list)
        self.current_question = data.question_list[0]
        self.index_of_current = 0

    def next_question(self):
        self.index_of_current = data.question_list.index(self.current_question)
        try:
            self.current_question  = data.question_list[self.index_of_current+1]
            self.index_of_current = self.index_of_current + 1
            return True
        except:
            return False


