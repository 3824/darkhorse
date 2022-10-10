from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from model.setting import Base
from model.setting import ENGINE

class RaceUrl(Base):
    __tablename__ = "race_url"
    summary_url = Column("summary_url", String(50))
    race_url = Column("race_url", String(50), primary_key = True)