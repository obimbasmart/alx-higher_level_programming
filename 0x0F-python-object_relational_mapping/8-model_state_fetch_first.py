#!/usr/bin/python3

"""script that lists the first state object from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    _, user_name, passwd, db_name = sys.argv
    engine = create_engine(
        'mysql+mysqldb://localhost/{}'.format(db_name),
        connect_args={'user': user_name, 'password': passwd})

    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).first()

    if (first_state):
        print('{}: {}'.format(first_state.id, first_state.name))

    session.close()
