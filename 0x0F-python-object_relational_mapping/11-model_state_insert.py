#!/usr/bin/python3
"""script that adds the State object “Louisiana” to
   the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    latest = State(name='Louisiana')
    session.add(latest)
    session.commit()
    print("{}".format(latest.id))
    session.close()
