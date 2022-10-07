from pydoc import describe
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from model.setting import Base
from model.setting import ENGINE

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
    f_id = Column("f_id", String(20))
    ff_id = Column("ff_id", String(20))
    fm_id = Column("fm_id", String(20))
    m_id = Column("m_id", String(20))
    mf_id = Column("mf_id", String(20))
    mm_id = Column("mm_id", String(20))

    def __repr__(self):
        return "{}({}), (f_id={})".format(self.name, self.id, self.f_id)
