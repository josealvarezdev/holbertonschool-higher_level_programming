#!/usr/bin/python3
''''Lists all State objects from the database hbtn_0e_6_usa'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})
    session.commit()
