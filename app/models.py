from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# Base class for all SQLAlchemy ORM models
Base = declarative_base()


# Model representing land use types (e.g., urban, agricultural)
class LandUse(Base):
    __tablename__ = "land_use"  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String, nullable=False)  # Name of the land use (required)
    hydrologi_soil_group = Column(String)  # Soil group associated with this land use (optional)
    default_cn = Column(Integer)  # Default curve number for runoff calculations (optional)
    
    # Relationship to the Watershed model, one LandUse can have many Watersheds
    watersheds = relationship("Watershed", back_populates="land_use")


# Model representing soil types (e.g., sandy, clay)
class SoilType(Base):
    __tablename__ = "soil_type"  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String, nullable=False)  # Name of the soil type (required)
    hydrologic_soil_group = Column(String)  # Soil group (optional)
    
    # Relationship to Watershed, one SoilType can be associated with many Watersheds
    watersheds = relationship("Watershed", back_populates="soil") 


# Model representing geographical regions
class Region(Base):
    __tablename__ = "region"  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String, nullable=False)  # Name of the region (required)
    
    # Relationship to Watershed, one Region can have many Watersheds
    watersheds = relationship("Watershed", back_populates="region")


# Model representing watersheds
class Watershed(Base):
    __tablename__ = "watershed"  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String, nullable=False)  # Watershed name (required)
    area_hectares = Column(Float, nullable=False)  # Size of the watershed in hectares
    land_use_id = Column(Integer, ForeignKey("land_use.id"))  # Foreign key linking to LandUse
    soil_type_id = Column(Integer, ForeignKey("soil_type.id"))  # Foreign key linking to SoilType
    region_id = Column(Integer, ForeignKey("region.id"))  # Foreign key linking to Region

    # ORM relationships to access related objects
    land_use = relationship("LandUse", back_populates="watersheds")
    soil = relationship("SoilType", back_populates="watersheds")
    region = relationship("Region", back_populates="watersheds")
    
    # Relationship to RainfallEvent, one Watershed can have many rainfall events
    rainfall_events = relationship("RainfallEvent", back_populates="watershed")


# Model representing rainfall events for a watershed
class RainfallEvent(Base):
    __tablename__ = "rainfall_event"  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary key
    date = Column(Date, nullable=False)  # Date of the rainfall event
    rainfall_mm = Column(Float, nullable=False)  # Rainfall amount in millimeters
    watershed_id = Column(Integer, ForeignKey("watershed.id"))  # Link to Watershed

    # Relationship to access the associated Watershed and runoff calculation object
    watershed = relationship("Watershed", back_populates="rainfall_events")
    runoff_calculations = relationship("RunOffCalculation", back_populates="rainfall_event") 


# Model representing runoff calculations for a rainfall event and watershed
class RunOffCalculation(Base):
    __tablename__ = "runoff_calculation"  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary key
    rainfall_id = (Integer, ForeignKey("rainfall_event.id"))  # Foreign key linking to RainfallEvent
    watershed_id = Column(Integer, ForeignKey("watershed.id"))  # Foreign key linking to Watershed
    cn_used = Column(Integer)  # Curve number used for this calculation
    run_off_depth_mm = Column(Float)  # Calculated runoff depth in millimeters
    run_off_volume_m3 = Column(Float)  # Calculated runoff volume in cubic meters
    time_stamp = Column(DateTime, default=datetime.utcnow)  # Timestamp of calculation (default now)
     
    # Relationships to access linked RainfallEvent and Watershed objects
    rainfall_event = relationship("RainfallEvent", back_populates="runoff_calculations")
    watershed = relationship("Watershed", back_populates="runoff_calculations")
