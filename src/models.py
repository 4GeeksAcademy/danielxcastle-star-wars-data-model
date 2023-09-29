import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    weapon = Column(String(250))
    location = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    galaxy = Column(String(250))
    top_locations = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    planet = Column(String(250))
    inhabitants = Column(String(250))
    top_locations = Column(String(250))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship("Planets")

class Weapons(Base):
    __tablename__ = 'weapons'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    damage = Column(Integer)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship("Characters")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
