from app.db.connection import LocalSession


def get_db_session():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()
