from sqlalchemy.orm import Session
from app.db.models import Category as CategoryModel
from app.schemas.category import (
    Category as CategorySchema,
)


class CategoryUseCases:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def add_category(self, category: CategorySchema):
        category_model = CategoryModel(**category.dict())
        self.db_session.add(category_model)
        self.db_session.commit()
        self.db_session.refresh(category_model)
        return category_model

    def list_categories(self):
        categories_on_db = self.db_session.query(CategoryModel).all()
        categories = [
            CategorySchema.from_orm(category) for category in categories_on_db
        ]
        return categories
