from ClassDefinitions import *
import datetime
import class Question()
import Persist


class Quiz:    #alexandria coffey
    """ Class Quiz is a class designed to get the base information for this project so
    that each user can have methods to use for getting questoinis for the quiz and entering
    questions etc to the quiz. This class lets the instructor to make questions and answers
    for a quiz that a user can take the quiz throguh the methods:
            Methods:
            Show_Quiz_ID - returns the ID of user
            Current_AllowedAttempts - return amount of allowed attempts at quiz
            setAllowedAttempts- setting the allowed attempts that a user has at a quiz
            show_Questions - return list of question objects belonging to quiz
            modifyQuestionTextQuestion - is letting the instructor modify any question(text)
            weight- returns the weight of each quiz
            show_Questions - lets the instructor access all questions at once, and from q.Bank
            Construct a quiz
                    Raises:
                        ValueError - (not int)
                    Return: Quiz object
        """

    def __init__(self, quizID, allowedAttempts, allowedTime): #alex
        self._quizID = quizID
        self._allowedAttempts = allowedAttempts
        self._allowedTime = allowedTime
        self._questions = []  # question objects in her
        self._user = user
        self.makeQuiz = makeQuiz

        _Quiz = Perist.getQuiz(quiz)
        _quizID = Persist.getQuizID(quiz)
        _Question = Persist.getQuestion(question)
        _instructorID = Persist.getUserID(userID)

    def getUser(self, userID, password, instrcutor):
        """This method is to check if the userID and password that a person
        enters is a instructor. If it is instrctor return boolean True, else
        raise keyError and get a error message "already in use" and return boolean
        False.
        """
        if self._quizID == "Instructor":
            return True
        else:
            raise KeyError("UserID already in use")
            return boolean(False)


    def makeQuiz(self, num):   #author: Alexandria Coffey
        """MakeQuiz runs through the question class a number of times using a
        while loop depending on how many questions instructor wants for quiz
        """
        while num != 0:
            if num == 0:
                break
            new_question = str(input("input question")) #question
            correct_ans = str(input("Input correct answer")) # correct answer
            answer = " "  # text that user studentAnswers
            answers = [correct_ans]
            while answer != "":
                answer = str(input("Input other possible answers, press enter to quit"))  # possible answers
                if answer != "":
                    new_q = Question(new_question, answers, correct_ans, 1)
                    self._questions.append(new_q)

                    num -= 1
            Persist.authenticate(userID)._Quiz[isInstructor]


    def Show_Quiz_ID(self):
        """Show quizID acts as a method to check if the quiz id is
        a valid one, and whether it will be used or not.
        Return the quizID
        """
        return self._quizID

    def Current_AllowedAttempts(self):
        """ Get allowed attempts at quiz
            Return the allowed attempts
        """
        return self._allowedAttempts
        Current_AllowedAttempts = Persist.getQuiz['allowedAttempts']._allowedAttempts

    def show_Questions(self):
        """Access the questions all at once
        return the list of questions from question bank
        """
        return self._questions
        show_Questions = Persist.getQuiz['question']._startTime


    def addQuestion(self, question):  # adding a question to the quiz is this done in while loop
        """This method will allow the instrcutor to add a question to the list of questions
            This will also append the question to question bank
            param: question
            Append the question to list of original questions
        """
        self._questions.append(question)  # appending question
        addQuestion = Persist.getQuiz['question']._questions

    def removeQuestion(self, q_index):  # remove question with the given index
        """ Removing a question from question bank...
        This will also remove question from question bank
        param: q_index - Accessing a question to remove from questions and question bank
        remove: The question from a specific index
        """
        self._questions.remove(self._questions[q_index])
        removeQuestion = Persist.getQuiz[q_index]._questions


    def QuizStartTime(self):
        """This is a method to get the initial statt time of the quiz,
        when the quiz should start and should:
        return the int initial start time of quiz
        """
        return self._startTime
        QuizStartTime = Persist.getQuiz[_allowedTime]._startTime


    def modifyQuizStartTime(self, new_StartTime):
        """Setting/modifying the quiz with a new start time
        args: new_StartTime
        set _startTime to a new int _startTime
        """
        self._startTime = new_StartTime
        modifyQuizStartTime = Persist.getQuiz[_allowedTime]._startTime

    def show_QuizEndTime(self):
        """Getting the quiz original end time
        return end time of quiz
        """
        return self._endTime
        show_QuizEndTime = Persist.getQuiz[allowedTime]._endTime

    def new_EndTime(self, new_EndTime):
        """Set a new quiz end time for studnets
        args: new_EndTime
        Set the value of the _endTime to a new int _endTime
        """
        self._endTime = new_EndTime
        new_QuizEndTime = Persist.getQuiz[allowedTime]._endTime

    def setAllowedAttempts(self, new_count):
        """setAllowedAttempts puts a limit on the number of attempts made at this quiz which
        will be used for preventing the student from going past their max attempts
        Setting the allowed attempts at quiz to a new_count
        Allowd a certain amount of attempts.
        This lets the user to change the number of attempts to any amount of attempts at quiz
        that is needed.
        """
        self._allowedAttempts = new_count  # changing the number of attempts


#question class

    def show_QuestionText(self):
        """This displays the question text of each question.
        """
        return str(self.show_QuestionText)
        Persist.getQuiz(user)._Quiz[quizID]


    def copyQuestion(self, question, possibleAnswers, correctAnswers, value):
        """Copy will create a identical question in the quesiton bank.
            return the idential question that the question bank stores
        """
        return Question(self._question, self._possibleAnswers, self._correctAnswers, self._value)
#        copyQuestion = Persist.getQuiz[]._endTime['']

    def show_PossibleAnswers(self):
        """This method lets the user enter possible answers for each
        quiz and returns the list of possible answers to the student.
        """
        return self._possibleAnswers

    def getCorrectAnswer(self):
        """This allowes the instrucot tGet the correct answer for each question
        Return the correct asnwer so the instructor can mark
        """
        return self._correctAnswer
        Persist.getStudentAnswers(userID)._Quiz[quizID]
        return ClassDefinitions.CompletedQuiz(Quiz(1, 1, [Question("What's CS stand for?", ["Computer Science", "Crumby Student"], ["Computer Science"], 10)]), 1, ["Computer Science"])


    def questionValue(self, question_value=2):
        """Get the value
        return the list of questions with the value
        """
        Persist.getquestionValue(user)._Quiz[question_value == 2]
        return self._value


    def modifyValue(self, new_value): #method for modifying value of question
        """This is a function to modify the value of a question
        args: new_value
        set the new value = current value
        """
        self._value = new_value
        Persist.setmoidfyValue(user)._Quiz[quizID]


    def modifyQuestionText(self, new_text):
        """
        param: new_text - change the text of the question a method to modify q_index is which question were changing
        Modify the list of questions with any index set with new text
        """
        self._question = new_text
        Persist.setmodifyQuestionText(new_text)._Quiz[quizID]

    def setQuestionPossibleAnswers(self, q_index,newOptions):  # method to create new possible asnwers new multiple choice answers
        """
        param: q_index, newOptions - method to create new possible answers/new mul choice answers
        the list of questions with any index set with new options, new possible answers
        """
        self._questions[user].setPossibleAnswers(newOptions)
        Persist.setQuestionPossibleAnswers(newOptions)._Quiz[quizID]
