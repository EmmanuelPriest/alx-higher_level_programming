#!/usr/bin/python3

'''script that lists all City objects from the database hbtn_0e_101_usa'''
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    createEngine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                                 format(sys.argv[1], sys.argv[2],
                                        sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=createEngine)
    create_sess = Session()

    state_city = create_sess.query(State).join(City).order_by(City.id).all()

    for state in state_city:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
