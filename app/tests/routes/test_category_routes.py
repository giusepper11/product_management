from fastapi.testclient import TestClient
from fastapi import status
from sqlalchemy.orm import Session
from app.main import app
from app.db.models import Category as CategoryModel

client = TestClient(app)


def test_add_category_route(db_session: Session):
    body = {"name": "Roupa", "slug": "roupa"}

    response = client.post("/category/add", json=body)
    category_id = response.json().get("id")
    category_on_db = (
        db_session.query(CategoryModel).filter(CategoryModel.id == category_id).all()
    )
    try:
        assert len(category_on_db) == 1
        assert response.status_code == status.HTTP_201_CREATED
    finally:
        db_session.delete(category_on_db[0])
        db_session.commit()


def test_list_category_route(categories_on_db):
    response = client.get("/category/list")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert len(data) == 4
    assert data[0] == {
        "name": categories_on_db[0].name,
        "slug": categories_on_db[0].slug,
        "id": categories_on_db[0].id,
    }
