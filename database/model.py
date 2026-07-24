import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from database.connection import Base


def make_id():
    return str(uuid.uuid4())


def current_time():
    return datetime.now(timezone.utc)


class User(Base):
    __tablename__ = "users"

    id = Column(
        String,
        primary_key=True,
        default=make_id,
    )


    username = Column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )


    password_hash = Column(
        String(255),
        nullable=False,
    )

    points = Column(
        Integer,
        default=0,
        nullable=False,
    )


    email_verified = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )


    created_at = Column(
        DateTime(timezone=True),
        default=current_time,
        nullable=False,
    )