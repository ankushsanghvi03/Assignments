from fastapi import FastAPI

from app.core.database import Base, engine

# Import models so SQLAlchemy registers them
from app.models.job import Job

app = FastAPI(
    title="Hiring Application"
)

# Create tables
Base.metadata.create_all(bind=engine)
print("Hiring Application Started Successfully")
print(f"Database file created at: {engine.url}")


@app.get("/")
def home():
    return {
        "message": "Hiring Application Started Successfully"
    }