from db.models.jobs import Job
from schemas.jobs import JobCreate
from sqlalchemy.orm import Session


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job_object = Job(**job.dict(), owner_id=owner_id)
    db.add(job_object)
    db.commit()
    db.refresh(job_object)
    return job_object


def retreive_job(id: int, db: Session):
    item = db.query(Job).filter(Job.id == id).first()  # select * from job where id = 1;
    return item


def list_jobs(db: Session):
    jobs = db.query(Job).filter(Job.is_active == True).all()
    return jobs


def update_job_by_id(id: int, job: JobCreate, db: Session, owner_id):
    existing_job = db.query(Job).filter(Job.id == id)
    # print(type(existing_job))
    # SELECT job.id AS job_id, job.title AS job_title, job.company AS job_company, job.company_url AS job_company_url,
    # job.location AS job_location, job.description AS job_description, job.date_posted AS job_date_posted,
    # job.is_active AS job_is_active, job.owner_id AS job_owner_id
    # FROM job
    # WHERE job.id = %(id_1)s
    if not existing_job.first():
        return 0
    # print(job.__dict__)
    # {'title': 'string', 'company': 'string', 'company_url': 'string', 'location': 'string',
    # 'description': 'string', 'date_posted': datetime.date(2023, 6, 14)}
    job.__dict__.update(
        owner_id=owner_id
    )  # update dictionary wit new key value of owner_id
    print(job)
    existing_job.update(job.__dict__)
    db.commit()
    return 1


def delete_job_by_id(id: int, db: Session, owner_id):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit()
    return 1


def search_job(query: str, db: Session):
    jobs = db.query(Job).filter(Job.title.contains(query))
    return jobs
