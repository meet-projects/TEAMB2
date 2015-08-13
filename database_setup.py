from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine



#PLACE YOUR TABLE SETUP INFORMATION HERE
Picture_Base= declarative_base()
class Picture(Picture_Base):
        __tablename__='picture'
        id=Column(Integer, primary_key=True)
        age= Column(String)
        gender=Column(String)
        nationality=Column(String)
        #user=Column(String)
        filename=Column(String)
        
User_Base= declarative_base()
class User(User_Base):
	__tablename__='user'
	id=Column(integer,primary_key=True)
	email=Column(String,primary_key=True)
	user_name=Column(String,primary_key=True)
	password=Column(String)

