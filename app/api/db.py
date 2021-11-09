import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database
from sqlalchemy.pool import StaticPool

DATABASE_URI = 'sqlite:///app/tmp.db'

engine = create_engine(DATABASE_URI, connect_args={"check_same_thread": False},  poolclass=StaticPool)
metadata = MetaData()


messages = Table(
    'messages',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('recipient', String(50)),
    Column('sender', String(50)),
    Column('message', String(2000)),
)

messages.create(bind=engine, checkfirst=False)
database = Database(DATABASE_URI)
