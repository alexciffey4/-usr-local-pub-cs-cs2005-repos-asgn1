"""Class definitions for online quiz service
    Classes:
        Course - A collection of users and associated quizzes
        User - A user of the online quiz tool
        Quiz - Quiz that users can take or edit
        Question - Question representations that reside within quizzes
        CompletedQuiz - Student answers for quizzes and attempt number
    Examples:
        <code>
            >>> x = User("BobLoblaw", "P@SSW0RD")
            >>> x.getUserID()
            "BobLoblaw"
            >>> x = Quiz("q1", 1, 3)
            >>> x.getAllowedAttempts()
            3
            >>> x = Question()
        </code>
        author: Chris Smith
"""


class Course:   #chris smith
    """Collection of users and quizzes
    Methods:
        addStudent - Add a student to the course
        addCourseQuiz - Add a quiz to the course
        author: Chris Smith
    """

    def __init__(self, courseName, instructorID):
        """Construct a Course object
        Raises:
          KeyError - instructorID does not exist
        Return: Course object
        """
        self._courseName = courseName
        self._instructorID = instructorID
        self._students = []
        self._quizzes = []


    def addStudent(self, userID):
        """Add a student to the Course
        Raises:
          KeyError - userID does not exist
        Return: boolean indicating success of operation
        """

        return True

    def addCourseQuiz(self, quizID):
        """Add a quiz to the Course
        Raises:
          KeyError - quizID does not exist
        Return: boolean indicating success of operation
        """

        return True

    def getStudents(self):
        return self._students

    def getQuizzes(self):
        return self._quizzes


class User:  #author : Chris Smith
    """System user (student or instructor)

        Author: Chris Smith
    """

    def __init__(self, userID, password, name, instructor=False):
        """Construct a user

            Attributes:
              _userID - unique string that contains user's username
              _password - string the contains user's password
              _name - string that contains user's first and last name
              _instructor - boolean indicating if user is instructor
              _completedQuizzes - a list of quizzes completed by user
              _courses - a list of courses being taken by the user

            Returns: user object
        """
        self._userID = userID
        self._password = password
        self._name = name
        self._completedQuizzes = []  # completedQuiz objects in here
        self._instructor = instructor
        self._courses = []


class Quiz:    #Alexandria Coffey
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
        """Construct a quiz
        Raises:
            ValueError - allowedAttempts or allowedTime not int
        Return: Quiz object
        """

class Question:  #Author Alexandria Coffey
"""System user
Class Question is a class designed to get questions for each quiz and promts the instructor to enter
a possible answer or correct answer. It tells us that each
that each user can have methods to use for getting questoinis for the quiz and entering
questions etc to the quiz. This class lets the instructor to make questions and answers
for a quiz that a user can take the quiz throguh the methods:
    Methods:
        copyQuestion - returns the identical question(copied)
        show_PossibleAnswers - return list of possible correct answers
        getCorrectAnswers - return list of correct answers
        questionValue - return value of question
        modifyValue - set a question to a value
        modifyQuestionText - set list of possible answers
        setQuestionPossibleAnswers - set list of correct answers
    """

    def __init__(self, question="", possibleAnswers=[], correctAnswers=[], questionValue=1):
        self._question = question  # question string here
        self._possibleAnswers = possibleAnswers  # list of strings here
        self._correctAnswers = correctAnswers  # need a list here too (in case of multiple correct answers)
        self._value = questionValue  # int


class CompletedQuiz:
    """Object to represent a student's quiz attempt
    Methods:
        getCompletedQuiz - return quiz taken by user
        getAttempt - return attempt number of given quiz
        getStudentAnswers - return student's responses to given quiz
    """

    def __init__(self, quiz, attempt, studentAnswers):
        """Constructor for CompletedQuiz class"""
        self._quiz = quiz  # Quiz object
        self._attempt = attempt  # 1, 2, 3...
        self._studentAnswers = studentAnswers  # list of strings ie ["a","c","d","a"]

    def getCompletedQuiz(self):
        """Get quiz taken by student user
            return: quiz object
        """
        return self._quiz

    def getAttempt(self):
        """Get attempt
            return: attempt number of quiz
        """
        return self._attempt

    def getStudentAnswers(self):
        """Get student's responses
            return: list of student responses
        """
        return self._studentAnswers
