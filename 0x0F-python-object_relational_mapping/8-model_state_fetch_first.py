#!/usr/bin/python3

'''
script that prints the first State object from
the database hbtn_0e_6_usa
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    createEngine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                                 format(sys.argv[1], sys.argv[2],
                                        sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=createEngine)
    create_sess = Session()

    states = create_sess.query(State).order_by(State.id).first()

    if not states:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
