import os
import sys
import data_orm
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from dateutil import parser
import geocoder

Base = declarative_base()

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key = True)
    LocationName = Column(String,ForeignKey('users.Location'))
    CityName = Column(String)
    StateName = Column(String)
    CountryName = Column(String)
    Offset = Column(String)
    Left = Column(Float)
    Right = Column(Float)
    Top = Column(Float)
    Bottom = Column(Float)

    def __init__(self, id, LocationName, CityName, StateName, CountryName, Offset, Left, Right, Top, Bottom):
        self.id = id
        self.LocationName = LocationName
        self.CityName = CityName
        self.StateName = StateName
        self.CountryName = CountryName
        self.Offset = Offset
        self.Left = Left
        self.Right = Right
        self.Top = Top
        self.Bottom = Bottom


        


