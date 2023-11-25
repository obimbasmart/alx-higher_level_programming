#!/usr/bin/env python3

"""script that lists the first state object from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import ProgrammingError
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    _, user_name, passwd, db_name = sys.argv
    engine = create_engine(
        'mysql+mysqldb://localhost/{}'.format(db_name),
        connect_args={'user': user_name, 'password': passwd})

    if Base.metadata.tables.get("states") is not None:  # no table
        Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California", cities=[
        City(name="San Francisco")])

    session.add(new_state)
    session.commit()
    session.close()
