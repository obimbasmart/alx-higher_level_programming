#!/usr/bin/python3

"""script that lists the first state object from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    _, user_name, passwd, db_name = sys.argv
    engine = create_engine(
        'mysql+mysqldb://localhost/{}'.format(db_name),
        connect_args={'user': user_name, 'password': passwd})

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California", cities=[City(name="San Francisco")])
    session.add(new_state)
    session.commit()
    session.close()
