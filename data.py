import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from sqlalchemy import (update, insert, and_)
Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    PostTypeId = Column(Integer)
    AcceptedAnswerId = Column(Integer)
    ParentId = Column(Integer)
    CreationDate = Column(DateTime)
    Score = Column(Integer)
    OwnerUserId = Column(Integer)
    LastActivityDate = Column(DateTime)
    Tags = Column(String)
    AnswerCount = Column(Integer)

class Users(Base):
	__tablename__ = 'users'
	Id = Column(Integer, primary_key= True)
	Reputation = Column(Integer)
	Location = Column(String)
	Views = Column(Integer)
	UpVotes = Column(Integer)
	DownVotes = Column(Integer)
	Age = Column(Integer)		

	def __init__(self, Id, Reputation, Location, Views, UpVotes, DownVotes, Age):
		self.Id= Id
		self.Reputation = Reputation
		self.Location = Location
		self.Views = Views
		self.UpVotes = UpVotes
		self.DownVotes = DownVotes
		self.Age = Age
	
	def __str__(self):
		return unicode(self).encode('utf-8')

engine = create_engine('sqlite:///stackoverflow.db') 
Base = declarative_base()
Base.metadata.create_all(engine)
Session = scoped_session(sessionmaker(bind=engine))

#Session.execute(insert(Users).values(Id = 123, Reputation = 21, Location= "test", Views= 2, UpVotes = 2, DownVotes = 3, Age = 22))
#Session.commit()
