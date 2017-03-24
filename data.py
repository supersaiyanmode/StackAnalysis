import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, Float, String, DateTime
from sqlalchemy import UniqueConstraint, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship,scoped_session
from sqlalchemy.interfaces import PoolListener


Base = declarative_base()


poststags_table  = Table('poststags',Base.metadata,
							Column('PostsId', Integer(), ForeignKey('questions.Id')),
							Column('TagsId', Integer(), ForeignKey('tags.id')))


class Posts(Base):
	__tablename__ = 'posts'

	id = Column(Integer, primary_key=True)
	PostTypeId = Column(Integer)
	AcceptedAnswerId = Column(Integer)
	ParentId = Column(Integer)
	CreationDate = Column(DateTime)
	Score = Column(Integer)
	OwnerUserId = Column(Integer, ForeignKey('users.Id'))
	LastActivityDate = Column(DateTime)
	Tags = Column(String)
	AnswerCount = Column(Integer)


class Questions(Base):
	__tablename__ = 'questions'

	Id = Column(Integer, primary_key=True)
	PostTypeId = Column(Integer)
	AcceptedAnswerId = Column(Integer)
	CreationDate = Column(DateTime)
	Score = Column(Integer)
	OwnerUserId = Column(Integer, ForeignKey('users.Id'))
	LastActivityDate = Column(DateTime)
	AnswerCount = Column(Integer)


class Answers(Base):
	__tablename__ = 'answers'

	Id = Column(Integer, primary_key=True)
	PostTypeId = Column(Integer)
	ParentId = Column(Integer)
	CreationDate = Column(DateTime)
	Score = Column(Integer)
	OwnerUserId = Column(Integer, ForeignKey('users.Id'))
	LastActivityDate = Column(DateTime)


class Tags(Base):
	__tablename__ = 'tags'

	id = Column(Integer, primary_key=True)
	TagName = Column(String,index = True, unique = True)
	questions = relationship("Questions", secondary = poststags_table)

	__table_args__ = (UniqueConstraint("TagName"),)

class Location(Base):
	__tablename__ = 'locations'

	id = Column(Integer, primary_key = True, autoincrement= True)
	location = Column(String(convert_unicode=True))
	city = Column(String(convert_unicode=True))
	state = Column(String(convert_unicode=True))
	country = Column(String(convert_unicode=True))
	timezone = Column(String)
	left = Column(Float)
	right = Column(Float)
	top = Column(Float)
	bottom = Column(Float)

class Users(Base):
	__tablename__ = 'users'

	Id = Column(Integer, primary_key= True)
	Reputation = Column(Integer)
	Location = Column(String(convert_unicode=True))
	Views = Column(Integer)
	UpVotes = Column(Integer)
	DownVotes = Column(Integer)
	Age = Column(Integer)	
	posts = relationship ('Posts', backref = 'users', lazy = 'dynamic')
	questions = relationship('Questions', backref = 'users')
	answers = relationship('Answers', backref = 'users')


class ForeignKeysListener(PoolListener):
    def connect(self, dbapi_con, con_record):
        db_cursor = dbapi_con.execute('pragma foreign_keys=ON')

listeners = [ForeignKeysListener()]
engine = create_engine('sqlite:///' + sys.argv[1], listeners=listeners)
Base.metadata.create_all(engine)
Session = scoped_session(sessionmaker(bind=engine))

