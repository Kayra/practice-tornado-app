from datetime import datetime
import secrets

from sqlalchemy import Column, Unicode, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from tornado_sqlalchemy import declarative_base


Base = declarative_base()


class Task(Base):
    """
    Tasks for the To Do list.
    """

    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    note = Column(Unicode)
    creation_date = Column(DateTime, nullable=False, default=datetime.now())
    due_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="tasks")

    def columns_to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            if isinstance(getattr(self, key), datetime):
                dict_[key] = getattr(self, key).isoformat()
            else:
                dict_[key] = getattr(self, key)
        return dict_


class User(Base):
    """
    The User object that owns tasks.
    """

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode, nullable=False)
    email = Column(Unicode, nullable=False)
    password = Column(Unicode, nullable=False)
    date_joined = Column(DateTime, nullable=False, default=datetime.now())
    token = Column(Unicode, nullable=False, default=secrets.token_urlsafe(64))
    tasks = relationship("Task", back_populates="user")
