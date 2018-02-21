from datetime import datetime
import secrets

from sqlalchemy import Column, Unicode, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from tornado_sqlalchemy import declarative_base


Base = declarative_base


class Task(Base):
    """
    Tasks for the To Do list.
    """
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    note = Column(Unicode)
    creation_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("user", back_populates="tasks")

    def __init__(self, *args, **kwargs):
        """
        On construction, set date of creation.
        """
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()


class User(Base):
    """
    The User object that owns tasks.
    """
    id = Column(Integer, primary_key=True)
    username = Column(Unicode, nullable=False)
    email = Column(Unicode, nullable=False)
    password = Column(Unicode, nullable=False)
    date_joined = Column(DateTime, nullable=False)
    token = Column(Unicode, nullable=False)
    tasks = relationship("Task", back_populates="user")

    def __init__(self, *args, **kwargs):
        """
        On construction, set date of creation.
        """
        super().__init__(*args, **kwargs)
        self.date_joined = datetime.now()
        self.token = secrets.token_urlsafe(64)
