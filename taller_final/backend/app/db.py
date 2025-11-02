# TODO: engine/session for SQLite (SQLModel). Read SQLITE_URL from env.
from sqlmodel import SQLModel, create_engine, Session
import os
SQLITE_URL = os.getenv("SQLITE_URL","sqlite:///app.db")
engine = create_engine(SQLITE_URL, echo=False)

def init_db():
    # TODO: SQLModel.metadata.create_all(engine)
    pass

def get_session():
    # TODO: yield a session
    # with Session(engine) as s: yield s
    raise NotImplementedError("get_session not implemented")
