import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "password"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or "sqlite:////tmp/test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
