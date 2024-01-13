#!/usr/bin/python3
""" prints first State objects from the database """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    state = State(name="California")

    city = City(name="San Francisco")

    state.cities.append(city)

    session.add_all([city, state])
    session.commit()
    session.close()
