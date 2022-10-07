# from dark_horse.model.setting import Base
from model.setting import Base
from sqlalchemy import Column, Integer, String, Float, Date

class RaceInfo(Base):
    __tablename__ = "race_info"
    race_id = Column("race_id", String(20), primary_key = True)
    cource = Column("cource", String(20))
    direction = Column("direction", String(20))
    distance = Column("distance", Integer)
    weather = Column("weather", String(20))
    condition = Column("condition", String(20))
    race_date = Column("race_date", Date)

    def __repr__(self):
        return "{}, {}, {} ({}, {}) - {}".format(self.cource, self.direction, self.distance, self.weather, self.condition, self.race_date)
