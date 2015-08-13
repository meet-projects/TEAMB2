from flask import Flask, render_template,request,redirect,url_for
from flask import session as web_session
import random
app = Flask(__name__)

#SQLAlchemy stuff
from database_setup import  Picture_Base, Picture 
#from database_setup import  User_Base
from database_setup import  User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Picture_Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()

admin = User(user_name='Admin', email='email@admin.com', password='admin')
#session.add(admin)
session.commit()
#YOUR WEB APP CODE GOES HERE
sofo=Picture(age='21-30',gender='male',nationality='eastern europe+former soviet union',filename='sofo.jpg')
#session.add(sofo)
session.commit()
roni=Picture(age='13-20',gender='male',nationality='middle east',filename='roni.png')
#session.add(roni)
ramesh=Picture(age='21-30',gender='male',nationality='north america',filename='ramesh.png')
#session.add(ramesh)
george=Picture(age='21-30',gender='male',nationality='north america',filename='george.png')
#session.add(george)
musa=Picture(age='13-20',gender='male',nationality='middle east',filename='musa.png')
#session.add(musa)
taylor=Picture(age='21-30',gender='female',nationality='north america',filename='taylor.jpg')
#session.add(taylor)
noor=Picture(age='13-20',gender='female',nationality='middle east',filename='noor.jpg')
#session.add(noor)
session.commit()
@app.route('/')
def main():
	
	return render_template('main_page.html')
@app.route('/')
def logout():
	web_session.pop('user_name',None)
	return redirect(url_for('go_home'))

@app.route('/profile')
def profile():
	if 'user_name' in web_session:
		return render_template('profile.html')
	
	
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
				return redirect(url_for('correct_submit',id=id))
	
	return redirect(url_for('wrong_submit',id=id))

@app.route('/game/show_answer/<int:id>')
def show_answers(id):
	picture=session.query(Picture).filter_by(id=id).first()	
	return render_template('show_answers.html', picture=picture)


@app.route('/game/correct/<int:id>')
def correct_submit(id):
	picture=session.query(Picture).filter_by(id=id).first()
	return render_template("correct.html",picture=picture)
@app.route('/game/wrong/<int:id>')
def wrong_submit(id):
	picture=session.query(Picture).filter_by(id=id).first()
	return render_template("false.html",picture=picture)
@app.route('/')
def go_home():
	return render_template("main_page.html")
@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
	if request.method=='GET':
		return render_template("sign_up.html")
	else:
		user_email=request.form['email']
		#return "got here"
		user_user_name=request.form['username']
		
		user_password=request.form['password']
		
		user=User(user_name=user_user_name, password=user_password,email=user_email)
		
		session.add(user)
		session.commit()
		return redirect(url_for('sign_in'))

@app.route('/sign_in',methods=['GET','POST'])
def sign_in():
	if request.method=='GET':
		return render_template("sign_in.html")
	else:
		x = session.query(User).filter_by(password=request.form['password'],user_name=request.form['username']).all()                                   
		if len(x) > 0:
			web_session['user_name']=request.form['username']
			return redirect(url_for('profile'))
		return render_template('sign_in.html')
@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method=='GET':
		return render_template("upload.html")
	else:
		new_pic=Picture(age=request.form['age'],gender=request.form['gender'],nationality=request.form['nationality'],filename=request.form['url'])

		session.add(new_pic)
		session.commit()
		return redirect('profile')			
			
app.secret_key='a'			
    
if __name__ == '__main__':
    app.run(debug=True)


