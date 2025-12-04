from app.db import init_db, SessionLocal
from app.models import LandUse, SoilType, Region, Watershed

# Function to populate the database with initial/default data
def seed():
    # Initialize the database and create tables if they don't exist
    init_db()

    # Create a new database session
    session = SessionLocal()

    # Define default land use types
    land_use = [
        LandUse(name="Urban", hydrologic_soil_group="C", default_cn=92),
        LandUse(name="Agriculture", hydrologic_soil_group="B", default_cn=75),
        LandUse(name="Forest", hydrologic_soil_group="A", default_cn=55),
    ]