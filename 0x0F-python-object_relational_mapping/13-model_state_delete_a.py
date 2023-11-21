#!/usr/bin/python3

"""script that deletes all State objects with a
name containing the letter a from the database  """

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

    states = session.query(State).filter(State.name.like("%a%")).all()

    [session.delete(state) for state in states]

    session.commit()
    session.close()
