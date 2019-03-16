# all the imports
import os
from classDefinitions import*

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)

clientpage = <p>""" &lt;!doctype html&gt;</p>
<p>Make Quiz!</p>
<div class="page">
<h1>Create Quiz</h1>
<form class="add-entry" action="http://localhost:5000/" method="post"><br />Enter a question:
<input name="Instructor" size="3" type="text" value="" /> <br /><input type="submit" value="Get the Answer"
/></form><!-- PLACEHOLDER --></div>
<p>"""

</p>


@app.route('/makeQuiz')
def makeQuiz():
    return _quiz
    
@app.route('/makeQuiz', methods=['quizID, userID, password'])
def getQuiz():
     = request.form['whatQuestion']
     = molecule.Molecule(chem).mass()

    msg = "Enter a" + " is " + str(question)
    return clientpage.replace('<!-- PLACEHOLDER -->', msg)

