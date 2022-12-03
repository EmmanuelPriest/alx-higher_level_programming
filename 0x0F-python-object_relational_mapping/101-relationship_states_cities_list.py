#!/usr/bin/pyhton3

'''
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
'''
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    create_engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                                  format(sys.argv[1], sys.argv[2],
                                         sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(create_engine)

    Session = sessionmaker(bind=create_engine)
    create_sess = Session()

    state_city = create_sess.query(State).outerjoin(City).
    order_by(State.id, City.id).all()

    for state in state_city:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
