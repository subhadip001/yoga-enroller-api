from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    name: str
    age: int
    email: str

class Enrollment(BaseModel):
    user_id: int
    batch: str
    month: int

class EnrollmentInputForPayment(BaseModel):
    enroll_id: int
    user_id: int
    month: int

class Payment(BaseModel):
    enroll_id: int
    user_id: int
    amount: int
    month: int
    status: str