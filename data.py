import os
import sys
from sqlalchemy import Column, ForeignKey,Float, Integer, String, DateTime,  UniqueConstraint, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship,scoped_session
#from dateutil import parser


Base = declarative_base()

poststags_table  = Table('poststags',Base.metadata,
                    Column('PostsId', Integer(), ForeignKey('posts.id')),
                    Column('TagsId', Integer(), ForeignKey('tags.id'))
                    )

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
    
    def __init__(self,id,PostTypeId,AcceptedAnswerId,ParentId,\
		CreationDate,Score,OwnerUserId,LastActivityDate,Tags,AnswerCount):
        self.id = id
        print self.AcceptedAnswerId," ",AcceptedAnswerId," ",PostTypeId," ",self.PostTypeId
        self.PostTypeId = PostTypeId
        self.AcceptedAnswerId = AcceptedAnswerId
        self.ParentId = ParentId
        self.CreationDate = parser.parse(CreationDate)
        self.Score = Score
        self.OwnerUserId = OwnerUserId
        self.LastActivityDate = parser.parse(LastActivityDate)
        self.Tags = Tags
        self.AnswerCount = AnswerCount
        
class Tags(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    TagName = Column(String,index = True, unique = True)
    posts = relationship("Posts", secondary = poststags_table)

    __table_args__ = ( 
                        UniqueConstraint("TagName"),
                     )

    def __init__(self, TagName):
        #self.id = id
        self.TagName = TagName


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key = True, autoincrement= True)
    location = Column(String,ForeignKey('users.Location'))
    city = Column(String)
    state = Column(String)
    country = Column(String)
    timezone = Column(String)
    left = Column(Float)
    right = Column(Float)
    top = Column(Float)
    bottom = Column(Float)

class Users(Base):
	__tablename__ = 'users'
	Id = Column(Integer, primary_key= True)
	Reputation = Column(Integer)
	Location = Column(String)
	Views = Column(Integer)
	UpVotes = Column(Integer)
	DownVotes = Column(Integer)
	Age = Column(Integer)

engine = create_engine('sqlite:///stackoverflow.db') 
Base.metadata.create_all(engine)
Session = scoped_session(sessionmaker(bind=engine))

