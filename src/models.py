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
    user_id = Column(Integer, ForeignKey('media.post_id'), primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    age = Column(Integer, nullable=True)

class media(Base):
    __tablename__ = 'media'
    post_id = Column(Integer, ForeignKey('post.likes'), ForeignKey('post.save'), ForeignKey('comment.text_comment'), primary_key=True)
    picture = Column(String)
    date_post = Column(String)
    comment_post = Column(String(200), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    user_id = Column(Integer, primary_key=True)
    comment_date = Column(String)
    text_comment = Column(String(200), ForeignKey('post.likes'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    likes = Column(Integer, primary_key=True)
    save = Column(String)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
