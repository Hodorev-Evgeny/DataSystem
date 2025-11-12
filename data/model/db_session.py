from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .local_setings import settings


def get_engine(user, password, host, port, database):
    url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(url)
    return engine

def get_engin_from_settings(settings):
    user = settings['pguser']
    password = settings['password']
    host = settings['host']
    port = settings['port']
    database = settings['pgdatabase']

    return get_engine(user, password, host, port, database)

def get_session():
    engine = get_engin_from_settings(settings)
    return sessionmaker(bind=engine, expire_on_commit=False)