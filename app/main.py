from fastapi import FastAPI
from app.routers.category_routes import router as category_routes

app = FastAPI()


@app.get("/health-check")
def health_check():
    return True


app.include_router(category_routes)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
