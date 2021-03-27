#!/usr/bin/python3
"""
9-model_state_filter_a.py
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
    for state in session.query(State).order_by(State.id).filter(
            State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
    session.close()
