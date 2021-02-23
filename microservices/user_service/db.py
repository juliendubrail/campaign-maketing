import os

from databases import Database
from sqlalchemy import (create_engine, MetaData, Column,
                        DateTime, Integer, String, Boolean, Table)
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
users = Table("users", metadata, Column("id", Integer, primary_key=True),
              Column("username", String(25)), Column("enabled", Boolean), Column("created_date", DateTime, default=func.now(), nullable=False),)


# databases query builder
database = Database(DATABASE_URL)
