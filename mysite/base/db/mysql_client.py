from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

mysql_config = {
    "user": "root",
    "passwd": "@professiona123",
    "host": "localhost",
    "port": "3306",
    "db": "mysite"
}

Base = declarative_base()

engine = create_engine('mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset=utf8mb4'.format(**mysql_config),
        pool_size=25,
        max_overflow=20,
        pool_recycle=3600,
        pool_pre_ping=True,
        encoding='utf-8',
        echo=False)


def MysqlSession():

    session_factory = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=True,
        expire_on_commit=True)
    return session_factory


db_session = MysqlSession()

