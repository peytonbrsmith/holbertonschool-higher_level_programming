#!/usr/bin/python3
"""
11
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    lousiana = State(name='Louisiana')
    session.add(lousiana)
    session.commit()
    print("{}".format(lousiana.id))
    session.close()
