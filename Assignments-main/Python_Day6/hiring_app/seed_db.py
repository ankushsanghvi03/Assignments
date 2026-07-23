from app.core.database import Base, engine
from app.core.session import SessionLocal
from app.models.job import Job


def main():
    # Ensure the table exists
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        job = Job(
            title="Backend Developer",
            description="Develop FastAPI applications and support hiring flows.",
            salary=750000.0,
            company="ABC Technologies"
        )
        db.add(job)
        db.commit()
        db.refresh(job)
        print("Inserted job:", {
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "salary": job.salary,
        })
    finally:
        db.close()


if __name__ == "__main__":
    main()
