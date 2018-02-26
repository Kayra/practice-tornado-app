import os

from sqlalchemy import engine_from_config

from todo.models import Base


def main():

    settings = {'sqlalchemy.url': os.environ.get('DATABASE_URL', 'postgres://localhost:5432/tornado_todo')}
    engine = engine_from_config(settings, prefix='sqlalchemy.')

    if bool(os.environ.get('DEBUG', '')):
        Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)
