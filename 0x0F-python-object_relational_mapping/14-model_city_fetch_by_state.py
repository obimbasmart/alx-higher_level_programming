#!/usr/bin/python3

""" that prints all City objects from the database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
import sys

if __name__ == "__main__":
    _, user_name, passwd, db_name = sys.argv
    engine = create_engine(
        'mysql+mysqldb://localhost/{}'.format(db_name),
        connect_args={'user': user_name, 'password': passwd})

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()
    for state, city in session.query(State, City).\
            filter(State.id == City.state_id).\
            all():
        print("{}: ({}) {}". format(state.name, city.id, city.name))

    session.commit()
    session.close()
