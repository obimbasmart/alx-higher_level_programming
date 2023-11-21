#!/usr/bin/python3

""" script that adds the State object “Louisiana” to the database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    _, user_name, passwd, db_name = sys.argv
    engine = create_engine(
        'mysql+mysqldb://localhost/{}'.format(db_name),
        connect_args={'user': user_name, 'password': passwd})

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State()
    new_state.name = "Louisiana"

    session.add(new_state)
    session.commit()

    state = session.query(State).filter(State.name == "Louisiana").first()
    print('{}'.format(state.id)) if state else print("Not found")
    session.close()
