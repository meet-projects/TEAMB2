from database_setup import  Picture_Base 
from database_setup import  Picture 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Picture_Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()

blake=Picture(age='21-30',gender='male',nationality='north america', filename='blake.png')
session.add(blake)
session.commit()
