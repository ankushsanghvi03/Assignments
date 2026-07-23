from pydantic import BaseModel, ConfigDict

class JobBase(BaseModel):
    title: str
    description: str
    salary: float
    company: str

class JobCreate(JobBase):
    pass

class JobUpdate(JobBase):
    title: str | None = None
    description: str | None = None
    salary: float | None = None
    company: str | None = None

class JobResponse(JobBase):
    id: int

    # class Config:
    #     form_attributes = True
    model_config = ConfigDict(form_attributes = True)
        

'''
JobBase - contains the common fields shared by all job schemas.
JobCreate - used when creating a new job (POST / jobs).
JobUpdate - used when updating a job (PUT or PATCH).
All fields are optional.
JobResponse - used when sending job details back to the client.
Includes the generated id.
'''
