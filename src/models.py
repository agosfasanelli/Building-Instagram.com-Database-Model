import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('comment.user_id'), primary_key=True)
    username = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    password = Column(nullable=False)

class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    picture = Column(String)
    date = Column(String)
    comment = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    text = Column(String(200), nullable=False)
    user_id = Column(Integer, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
