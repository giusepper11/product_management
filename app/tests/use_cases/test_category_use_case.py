from sqlalchemy.orm import Session
from app.use_cases.category import CategoryUseCases
from app.db.models import Category as CategoryModel
from app.schemas.category import Category as CategorySchema


def test_add_category_ac(db_session: Session):
    uc = CategoryUseCases(db_session)
    category = CategorySchema(id=None, name="roupa", slug="roupa")
    uc.add_category(category)

    category_on_db = db_session.query(CategoryModel).all()

    try:
        assert len(category_on_db) == 1
    finally:
        db_session.delete(category_on_db[0])
        db_session.commit()


def test_list_categories(db_session, categories_on_db):
    uc = CategoryUseCases(db_session=db_session)

    categories_schema = uc.list_categories()

    assert len(categories_schema) == 4
    assert type(categories_schema[0]) == CategorySchema
    assert categories_schema[0].id == categories_on_db[0].id
    assert categories_schema[0].name == categories_on_db[0].name
    assert categories_schema[0].slug == categories_on_db[0].slug
