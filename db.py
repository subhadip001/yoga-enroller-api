from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from sqlalchemy import CheckConstraint

db_url = os.getenv("DB_URL")

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    batch = Column(String)
    month = Column(Integer)
    __table_args__ = (
        CheckConstraint("month >= 1 AND month <= 12", name="check_month_range"),
    )


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    enroll_id = Column(Integer, ForeignKey("enrollments.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Integer)
    month = Column(Integer, ForeignKey("enrollments.month"))
    status = Column(String)


Base.metadata.create_all(bind=engine)
