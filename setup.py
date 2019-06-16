import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    phone = Column(String(250))
    address = Column(String(250))


class Group(Base):
    __tablename__ = 'Group'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class UserGroups(Base):
    __tablename__ = 'UserGroups'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)
    group_id = Column(Integer, ForeignKey('Group.id'))
    group = relationship(Group)


class Message(Base):
    __tablename__ = 'Message'

    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    sender_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)


    group_id=Column(Integer, ForeignKey('Group.id'))
    group=relationship(Group)

    created_date = Column(DateTime, default=datetime.datetime.utcnow)


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
