#!/usr/bin/env python

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer, Text, ForeignKey

from sqlalchemy.orm import relationship

engine = create_engine('mysql://root:@localhost/blog')
print(engine)
Base = declarative_base()

class Uesr(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref = 'author')
    userinfo = relationship('Userinfo', backref = 'user', uselist=False)


class UserInfo(Base):
    __tablename__ = 'userinfos'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    qq = Column(String(11))
    phone = Column(String(11))
    link = Column(String(64))
    user_id = Column(Integer, ForeignKey('users.id'))
    def __repr__(self):
        return 'UserInfo(name={})'.format(self.name)

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    def __repr__(self):
            return 'Article(title={})'.format(self.title)

Base.metadata.create_all(engine)

