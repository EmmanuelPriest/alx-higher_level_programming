#!/usr/bin/python3

'''script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
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

    new_state = State(name="Louisiana")
    create_sess.add(new_state)
    create_sess.commit()

    print("{}".format(new_state.id))
