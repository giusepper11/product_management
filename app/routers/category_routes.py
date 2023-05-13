from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from app.routers.deps import get_db_session
from app.schemas.category import Category
from app.use_cases.category import CategoryUseCases

router = APIRouter(prefix="/category", tags=["Category"])


@router.post(
    "/add",
    response_model=Category,
    status_code=status.HTTP_201_CREATED,
)
def add_category_route(
    category: Category,
    db_session: Session = Depends(get_db_session),
):
    uc = CategoryUseCases(db_session)
    return uc.add_category(category)


@router.get("/list")
def list_categories_route(db_session: Session = Depends(get_db_session)):
    uc = CategoryUseCases(db_session=db_session)
    categories = uc.list_categories()

    return categories
