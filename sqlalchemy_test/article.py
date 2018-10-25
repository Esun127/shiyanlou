#!/usr/bin/env python

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer, Text

from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship


engine = create_engine('mysql://root:@localhost/blog')
print(engine)
Base = declarative_base()

class Uesr(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64),nullable=False, index=True)
    articles = relationship('Article')

    def __repr__(self):
        return 'User(username={})'.format(self.username)

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User')
    #author = relationship('User', backref='articles')
    def __repr__(self):
        return 'Article(title={})'.format(self.title)

Base.metadata.create_all(engine)

