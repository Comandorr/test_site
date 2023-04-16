from flask import Flask, url_for, redirect, render_template
import random
from db_scripts import get_question

n_quiz = 0
n_quest = 0


def index():
    global n_quiz, n_quest
    n_quest = 0
    n_quiz = 0
    return render_template('start.html')


def test():
    global n_quiz, n_quest
    result = get_question(n_quiz, n_quest)
    if result == None:
        return redirect(url_for('result'))
    text = '<h3>' + result[1] + '</h3><ul>'
    v1 = '<li>' + result[2] + '</li>'
    v2 = '<li>' + result[3] + '</li>'
    v3 = '<li>' + result[4] + '</li>'
    v4 = '<li>' + result[5] + '</li></ul>'
    link = '<a href = "/test">Следующий вопрос</a>'
    n_quest += 1
    return text + v1 + v2 + v3 + v4 + link



def result():
    return '<h3>Поздравляем, вы завершили тест </h3> <br> <a href = "/">Вернуться на главную </a>'


app = Flask(__name__)
app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)
if __name__ == "__main__":
    app.run()