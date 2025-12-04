from sqlalchemy import Column, Integer, String, Float, ForeignKey,Date, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class LandUse(Base):
    __tablename__ = "land_use"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hydrologi_soil_group = Column(String)
    default_cn = Column(Integer)
    watersheds = relationship ("Watershed", back_populates="land_use")


