from sqlalchemy import func

from auth.passwords import hash_password
from database.connection import get_db
from database.models import User


def find_user_by_email(email):
    with get_db() as db:
        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if user is None:
            return None

        db.expunge(user)
        return user


def find_user_by_username(username):
    with get_db() as db:
        user = (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

        if user is None:
            return None

        db.expunge(user)
        return user


def create_user(username, email, password):
    password_hash = hash_password(password)

    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
    )

    with get_db() as db:
        db.add(user)
        db.flush()
        db.refresh(user)
        db.expunge(user)

    return user


def count_users():
    with get_db() as db:
        count = (
            db.query(func.count(User.id))
            .scalar()
        )

    return count or 0