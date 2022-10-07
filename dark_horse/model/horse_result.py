from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from model.setting import Base
from model.setting import ENGINE

class HorseResult(Base):
    __tablename__ = "horse_result"
    race_id = Column("race_id", String(20), primary_key = True)
    horse_id = Column("horse_id", String(20), primary_key = True)
    order_arrival = Column("order_arrival", Integer)
    frame_number = Column("frame_number", Integer)
    horse_number = Column("horse_number", Integer)
    time = Column("time", Integer)
    diff = Column("diff", Integer)
    weight = Column("weight", Integer)
    weight_diff = Column("weight_diff", Integer)

    def __repr__(self):
        return "{}({})".format(self.race_id, self.horse_id)
