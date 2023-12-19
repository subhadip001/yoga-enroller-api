from fastapi import FastAPI, Depends, HTTPException, Request, Response
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from db import SessionLocal, engine, User, Enrollment, Payment
from schemas import (
    User as UserSchema,
    Enrollment as EnrollmentSchema,
    Payment as PaymentSchema,
    EnrollmentInputForPayment,
)
import time

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    expose_headers=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/")
async def get_users(db: SessionLocal = Depends(get_db)):
    return db.query(User).all()


@app.post("/users/")
async def create_user(user: UserSchema, db: SessionLocal = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    if not 18 <= user.age <= 65:
        raise HTTPException(status_code=400, detail="Age must be between 18 and 65")

    try:
        db_user = User(name=user.name, age=user.age, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/enrollments/")
async def get_enrollments(db: SessionLocal = Depends(get_db)):
    return db.query(Enrollment).all()


@app.post("/enrollments/")
async def create_enrollment(
    enrollment: EnrollmentSchema, db: SessionLocal = Depends(get_db)
):
    db_user = db.query(User).filter(User.id == enrollment.user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    valid_batches = ["6-7AM", "7-8AM", "8-9AM", "5-6PM"]
    if enrollment.batch not in valid_batches:
        raise HTTPException(
            status_code=400,
            detail=f"Batch must be one of {valid_batches}",
        )

    try:
        db_enrollment = Enrollment(
            user_id=enrollment.user_id, batch=enrollment.batch, month=enrollment.month
        )
        db.add(db_enrollment)
        db.commit()
        db.refresh(db_enrollment)
        return db_enrollment
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


async def complete_payment(payment, db):
    db_payment = (
        db.query(Payment).filter(Payment.enroll_id == payment.enroll_id).first()
    )
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    time.sleep(5)
    try:
        db_payment.status = "completed"
        db.commit()
        db.refresh(db_payment)
        return db_payment
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/payments/")
async def create_payment(
    enrollment_input_for_payment: EnrollmentInputForPayment,
    db: SessionLocal = Depends(get_db),
):
    db_user = (
        db.query(User).filter(User.id == enrollment_input_for_payment.user_id).first()
    )
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_enrollment = (
        db.query(Enrollment)
        .filter(Enrollment.id == enrollment_input_for_payment.enroll_id)
        .first()
    )
    if not db_enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    db_payment = (
        db.query(Payment)
        .filter(Payment.enroll_id == enrollment_input_for_payment.enroll_id)
        .first()
    )
    if db_payment:
        raise HTTPException(status_code=400, detail="Payment already done")

    try:
        print("Making payment...")
        db_payment = Payment(
            enroll_id=enrollment_input_for_payment.enroll_id,
            user_id=enrollment_input_for_payment.user_id,
            amount=500,
            month=enrollment_input_for_payment.month,
            status="pending",
        )
        db.add(db_payment)
        db.commit()
        return await complete_payment(db_payment, db)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/payments/")
async def get_payments(db: SessionLocal = Depends(get_db)):
    return db.query(Payment).all()


@app.get("/")
async def root():
    return {"message": "This is a test"}


