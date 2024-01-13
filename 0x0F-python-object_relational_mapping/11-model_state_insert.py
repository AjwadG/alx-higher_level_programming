#!/usr/bin/python3
""" adds bot row / object to the DB """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == "Louisiana").first()
    if state is None:
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        print(new_state.id)
