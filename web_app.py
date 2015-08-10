from flask import Flask, render_template,request, session,redirect,url_for
import random
app = Flask(__name__)

#SQLAlchemy stuff
from database_setup import  Picture_Base 
from database_setup import  Picture 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Picture_Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE


@app.route('/')
def main():
	return render_template('main_page.html')

@app.route('/correct')
def correct() :
	return render_template('correct.html')



@app.route('/false')
def false() :
	return render_template('false.html')


@app.route('/game',methods=['GET','POST'])
def start_game():
    # pictures=session.query(Picture).all()
    # picture= random.choice(pictures)
    if request.method=='GET':
        pictures=session.query(Picture).all()
        picture= random.choice(pictures)
	return render_template("game.html",picture=picture)
    else:
        id=int(request.form['photo_id'])
        picture=session.query(Picture).filter_by(id=id).first()
	user_answer_age=request.form['age']
	user_answer_nationality=request.form['nationality']
	user_answer_gender=request.form['gender']
        #return "%s %s %s<br>%s %s %s" % (picture.age, picture.nationality, picture.gender, user_answer_age, user_answer_nationality, user_answer_gender)
        #return request.form['age']
	if user_answer_age== picture.age:
		if user_answer_nationality==picture.nationality:
			if user_answer_gender==picture.gender:
				return redirect(url_for('correct_submit'))
	
	return redirect(url_for('wrong_submit'))

@app.route('/game/correct')
def correct_submit():
    return render_template("correct.html")
@app.route('/game/wrong')
def wrong_submit():
    return render_template("false.html")
@app.route('/')
def go_home():
    return render_template("main_page.html")                                    
    
if __name__ == '__main__':
    app.run(debug=True)


