from app.db import init_db, SessionLocal
from app.models import LandUse, SoilType, Region, Watershed

# Function to populate the database with initial/default data
def seed():
    # Initialize the database and create tables if they don't exist
    init_db()

    # Create a new database session
    session = SessionLocal()

    # Define default land use types
    landUse = [
        LandUse(name="Urban", hydrologic_soil_group="C", default_cn=92),
        LandUse(name="Agriculture", hydrologic_soil_group="B", default_cn=75),
        LandUse(name="Forest", hydrologic_soil_group="A", default_cn=55),
    ]


    # Define default soil types
    soils = [
        SoilType(name="Sandy", hydrologic_group="A"),
        SoilType(name="Loam", hydrologic_group="B"),
        SoilType(name="Clay", hydrologic_group="D"),
    ]

    # Define default regions
    regions = [
        Region(name="Nairobi"),
        Region(name="Western Kenya"),
        Region(name="Coast"),
    ]


    # Add all default land uses, soils, and regions to the session
    session.add_all(landUse + soils + regions)

    # Commit changes to save them to the database
    session.commit()

    # Create a sample watershed using the seeded data
    ws = Watershed(
        name="Sample Watershed",
        area_hectares=150,
        land_use_id=1,  # Link to Urban land use
        soil_id=2,      # Link to Loam soil type
        region_id=1     # Link to Nairobi region
    )

    # Add the sample watershed to the session
    session.add(ws)

    # Commit changes to save the watershed
    session.commit()

    # Print a confirmation message
    print("Database seeded with default data.")

    # Close the database session
    session.close()


# Run the seed function when this script is executed directly
if __name__ == "__main__":
    seed()

