from user import User
from band import Band
from sqlalchemy import func


def count_user_ids(session):
    return session.query(func.count(User.id)).one()


def return_band_name_and_total_shows_histogram(session):
    return {b.name:len(b.shows)for b in session.query(Band).all()}
