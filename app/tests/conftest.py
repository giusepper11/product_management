import pytest
from sqlalchemy.orm import Session
from app.db.connection import LocalSession
from app.db.models import Category as CategoryModel


@pytest.fixture()
def db_session():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture()
def categories_on_db(db_session: Session):
    categories = [
        CategoryModel(name="Roupa", slug="roupa"),
        CategoryModel(name="Carro", slug="carro"),
        CategoryModel(name="Items de cozinha", slug="itens-de-cozinha"),
        CategoryModel(name="Decoracao", slug="decoracao"),
    ]

    db_session.add_all(categories)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)
    try:
        yield categories
    finally:
        for category in categories:
            db_session.delete(category)
        db_session.commit()
