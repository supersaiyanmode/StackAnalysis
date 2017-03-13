import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship,scoped_session
from dateutil import parser
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
    
    def __init__(self,id,PostTypeId,AcceptedAnswerId,ParentId,CreationDate,Score,OwnerUserId,LastActivityDate,Tags,AnswerCount):
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


engine = create_engine('sqlite:///posts.db') 
Base.metadata.create_all(engine)
Session = scoped_session(sessionmaker(bind=engine))

