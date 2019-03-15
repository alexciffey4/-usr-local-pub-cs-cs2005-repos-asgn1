import unittest
from ClassDefinitions import *


class CreateQuizTestMethods(unittest.TestCase):  #author Alexandria Coffey - ALL tests here

    def setUp(self):
        self.question = ClassDefinitions.Question(None, None, None, None)
        self.quiz = ClassDefinitions.Quiz("CS2005Q1", 3, 40)

        test_quiz = Quiz("Test Quiz", 3, None)
    	test_quiz.setQuizStartTime("4:20pm")
    	test_quiz.setQuizEndTime("1:00pm")
    	test_quiz.setAllowedAttempts(3)


    def testMakeQuiz(self):
        test_quiz = Quiz(None, None, None)
        test_quiz.makeQuiz(3)
        self.assertTrue(len(test_quiz._questions) == 3)

    def testcurrent_AllowedAttempts(self)
        test_quiz = Quiz(None, 4, None)
        self.assertTrue(test_quiz.Current_AllowedAttempts == 4)
        self.assertIn(self.quiz.['_allowedAttempts'])

    def testgetUser(self):
        test_quiz = Quiz(None, None, None)
        test_quiz.getUser(userID)
        self.assertTrue(test._Persist.getUser() == "Instructor")
        self.assertFalse(test._Persist.getUser() == "Student")

    def test_bad_current_AllowedAttempts(self):
        self.assertFalse(test_quiz.Current_AllowedAttempts == 2)

    def testQuizEndTime(self):   #testing and failing quiz end time
        test_quiz = Quiz(None, None, None)
        test_quiz._setQuizendTime = "1:00"
        self.assertTrue(test_quiz_QuizEndTime() == "1:00pm")
        self.assertIn(self.Quiz.persist.db['_endTime'])

    def test_bad_QuizEndTime(self):
        self.assertFalse(test_quizQuizEndTime() == "2:00pm")
        with self.assertRaises(ValueError): self.Quiz.Current_AllowedAttempts('')


    def testQuizStartTime(self):   #testing and failing quiz start time
        test_quiz = Quiz(None, None, None,None)
        test_quiz._setModifyingStartTime = "4:20"
        self.assertTrue(test_quiz._startTime() == "4:20pm")

    def test_bad_QuizStartTime(self):
        self.assertFalse(test_quiz._startTime() == "2:00pm")
        with self.assertRaises(ValueError): self.Quiz._startTime('2:00pm')


    def test_good_QuizAddQuestion(self):    #testing and failing when you add a question
        test_quiz = Quiz(None, None, None, None)    #3 params from question class
        test_quiz.set_good_quizAddQuestion("How many students in Comp 2005?")
        self.assertTrue(test_quiz.getQuizAddQuestion() == "How many students in Comp 2005?")
        self.assertIn(self.quiz.['addQuestion'])

    def test_bad_QuizAddQuestion(self):
        self.assertFalse(test_quiz.get_bad_QuizAddQuestion() == "How many students in comp 2001?"")
        with self.assertRaises(KeyError): self.quiz.getQuizAddQuestion("bad question")


    def test_good_QuizRemoveQuestion(self):   #testing and failing when you remove a question
        test_quiz = Quiz(None, None, None, None)
        test_quiz.set_good_quizRemoveQuestion("How many students in comp 2003?")
        self.assertTrue(test_quiz.getQuizRemoveQuestion() == "How many students in comp 2003?"

    def test_bad_QuizRemoveQuestion(self):
        self.assertFalse(test_quiz.get_bad_QuizRemoveQuestion() == "How many students are in Dr.Brown's class?")


    def test_good_QuizCopyQuestion(self):   #Testing questions to copy
        test_quiz = Quiz(None, None, None, None)
        test_quiz.setCopyQuestion("How many students in Dr.Browns class?", 2)

    def test_good_QuizCopyQuestion(self):
        self.assertTrue(test_quiz.getQuizCopyQuestion() == "How Many Students in Dr.Browns class?")

    def test_bad_QuizCopyQuestion(self):
        test_quiz = Quiz(None, None, None, None)
        self.assertFalse(test_quiz.getQuizStartTime() == "2:00pm")

    def testshow_QuestionText(self):
        test_question = Question("What is 1+1", None, None, None)
        self.assertTrue(test_question.show_QuestionText()== "What is 1+1")

    def test_bad_QuestionText(self):
        self.assertFalse(test_question.show_QuestionText()== "What is 4*4")

    def test_quizID(self):
        test_quiz = Quiz("1230", None, None)
        test_quizID = Quiz

    def test_good_isInstructor(self):
        self.assertTrue(Login.isInstructor("EBrown"))

    def test_userNotInstructor_isInstructor(self):
        self.assertFalse(Login.isInstructor("CSmith"))



if __name__ == '__main__':
    unittest.main()
