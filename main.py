from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap
import csv
class MovieForm(FlaskForm):
    movie=StringField('Movie Name', validators=[DataRequired()])
    imdblink=StringField('IMDB Link', validators=[DataRequired(), URL()])
    storyrate=SelectField('Story', validators=[DataRequired()], choices=["📜","📜📜","📜📜📜","📜📜📜📜","📜📜📜📜📜"])
    cinematography=SelectField('Cinematography', validators=[DataRequired()], choices=["📽️","📽️📽️","📽️📽️📽️","📽️📽️📽️📽️","📽️📽️📽️📽️📽️"])
    characters=SelectField('Characters', validators=[DataRequired()], choices=["👻","👻👻","👻👻👻","👻👻👻👻","👻👻👻👻👻"])
    cast=SelectField('Cast', validators=[DataRequired()], choices=["💜","💜💜","💜💜💜","💜💜💜💜","💜💜💜💜💜"])
    submit=SubmitField('Submit')

class BookForm(FlaskForm):
    book=StringField('Book Name', validators=[DataRequired()])
    booklink=StringField('Book Link', validators=[DataRequired(), URL()])
    storyrate=SelectField('Story', validators=[DataRequired()], choices=["📜","📜📜","📜📜📜","📜📜📜📜","📜📜📜📜📜"])
    fluency=SelectField('Fluency', validators=[DataRequired()], choices=["😯","😯😯","😯😯😯","😯😯😯😯","😯😯😯😯😯"])
    characters=SelectField('Characters', validators=[DataRequired()], choices=["👻","👻👻","👻👻👻","👻👻👻👻","👻👻👻👻👻"])
    submit=SubmitField('Submit')

app=Flask(__name__)
# app.config['SECRET_KEY']="your secret key"
bootstrap=Bootstrap(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addforbook', methods=['GET','POST'])
def addforbook():
    bookform=BookForm()
    if bookform.validate_on_submit():
        with open("book-data.csv", mode='a', encoding='UTF-8') as csv_file:
            csv_file.write(f"\n{bookform.book.data},"
                           f"{bookform.booklink.data},"
                           f"{bookform.storyrate.data},"
                           f"{bookform.fluency.data},"
                           f"{bookform.characters.data}")
        return redirect(url_for('books'))
    return render_template('bookadd.html',form=bookform)

@app.route('/books')
def books():
    with open("book-data.csv", newline='', encoding='UTF-8') as csv_file:
        csv_data=csv.reader(csv_file, delimiter=',')
        list_of_rows=[]
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('books.html')



@app.route('/addformovie', methods=['GET','POST'])
def addformovie():
    movieform=MovieForm()
    if movieform.validate_on_submit():
        with open("movie-data.csv", mode='a', encoding='UTF-8') as csv_file:
            csv_file.write(f"\n{movieform.movie.data},"
                           f"{movieform.imdblink.data},"
                           f"{movieform.storyrate.data},"
                           f"{movieform.cinematography.data},"
                           f"{movieform.characters.data},"
                           f"{movieform.cast.data}")
        return redirect(url_for('movies'))
    return render_template('moviadd.html',form=movieform)
@app.route('/movies')
def movies():
    with open("movie-data.csv", newline='', encoding='UTF-8') as csv_file:
        csv_data=csv.reader(csv_file, delimiter=',')
        list_of_rows=[]
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('movies.html')

if __name__=='__main__':
    app.run(debug=True)