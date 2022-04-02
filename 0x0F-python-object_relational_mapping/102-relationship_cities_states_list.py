#!/usr/bin/python3
"""
script that lists all City objects from the database
hbtn_0e_101_usa
"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
