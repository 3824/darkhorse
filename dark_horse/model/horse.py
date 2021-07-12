from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from dark_horse.model.setting import Base
from dark_horse.model.setting import ENGINE

class Horse(Base):
    __tablename__ = "horse"
    id = Column("id", String(20), primary_key = True)
    name = Column("name", String(20))
    birth = Column("birth", String(20))
    trainer = Column("trainer", String(20))
    owner = Column("owner", String(20))
    breeder = Column("breeder", String(20))
    hometown = Column("hometown", String(20))
    price = Column("price", Integer)
    get_price = Column("get_price", Integer)

    def __repr__(self):
        return "{}({})".format(self.name, self.id)
