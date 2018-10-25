#!/usr/bin/env python

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer


engine = create_engine('mysql://root:@localhost/blog')
print(engine)
Base = declarative_base()

class Uesr(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)

    def __repr__(self):
        return 'User(username={})'.format(self.username)


Base.metadata.create_all(engine)

