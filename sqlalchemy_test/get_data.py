#!/usr/bin/env python

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer, Text, ForeignKey, Table

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
    userinfo = relationship('UserInfo', backref = 'user', uselist=False)

    def __repr__(self):
        return 'Uesr(username={})'.format(self.username)


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
    cate_id = Column(Integer, ForeignKey('catagories.id'))
    # jian li duo dui duo guan xi
    tags = relationship('Tag', secondary='article_tag', backref='articles')
    def __repr__(self):
            return 'Article(title={})'.format(self.title)

article_tag = Table('article_tag', Base.metadata,
        Column('article_id', Integer, ForeignKey('articles.id')),
        Column('tag_id', Integer, ForeignKey('tags.id'))
        )

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return 'Tag(name={})'.format(self.name)



class Catagory(Base):
    __tablename__ = 'catagories'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='catagory')
    def __repr__(self):
        return 'Catagory(name={})'.format(self.name)

# yong ying she lei jian biao
#Base.metadata.create_all(engine)

from faker import Factory
from sqlalchemy.orm import sessionmaker
import random

Session = sessionmaker(bind=engine)
session = Session()
r = session.query(Uesr).get(1)
print(r)
r = session.query(Uesr).filter(Uesr.username == 'Timothy Whitehead').first()
print(r)
r = session.query(Uesr).all()
print(r)
a = session.query(Article).get(10)
print(a.tags, a.catagory, a.title)
