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



class SoilType(Base):
    __tablename__ = "soil_type"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hydrologic_soil_group = Column(String)
    watersheds = relationship("Watershed", back_populates="soil") 


class Region(Base):
    __tablename__ = "region"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    watersheds = relationship("Watershed", back_populates="region")

class Watershed(Base):
    __tablename__ = "watershed"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    area_hectares = Column(Float, nullable=False)
    land_use_id = Column(Integer, ForeignKey("land_use.id"))
    soil_type_id = Column(Integer, ForeignKey("soil_type.id"))
    region_id = Column(Integer, ForeignKey("region.id"))

    land_use = relationship("LandUse", back_populates="watersheds")
    soil = relationship("SoilType", back_populates="watersheds")
    region = relationship("Region", back_populates="watersheds")
    rainfall_events = relationship("RainfallEvent", back_populates="watershed")


