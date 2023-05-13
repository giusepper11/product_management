import pytest
from pydantic.errors import PydanticValueError
from app.schemas.category import Category


def test_category_schema():
    category = Category(id=None, name="Roupa", slug="roupa")

    assert category.dict() == {"id": None, "name": "Roupa", "slug": "roupa"}


def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        category = Category(id=None, name="Roupa", slug="roupa de cama")

    with pytest.raises(ValueError):
        category = Category(id=None, name="Roupa", slug="ção")

    with pytest.raises(ValueError):
        category = Category(id=None, name="Roupa", slug="Roupa")
