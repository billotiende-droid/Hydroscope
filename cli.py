from app.db import SessionLocal
from app.models import Watershed, LandUse, SoilType, Region
from app.crud import calculate_runoff_linked, list_runoff_calculations, add_rainfall_event
from datetime import datetime

# Function to add a new watershed interactively via user input
def add_watershed():
    # Create a new database session
    session = SessionLocal()

    # Prompt user to enter the watershed name
    name = input("Enter watershed name: ")

    # Prompt user to enter the watershed area in hectares
    area = float(input("Enter area in hectares: "))

    # Fetch all land use options from the database
    land_uses = session.query(LandUse).all()
    print("Select Land Use:")
    # Display land use options with ID, name, and default CN
    for lu in land_uses:
        print(f"{lu.id}: {lu.name} (CN: {lu.default_cn})")
    # Ask user to select land use by ID
    land_use_id = int(input("Land Use ID: "))

    # Fetch all soil types from the database
    soils = session.query(SoilType).all()
    print("Select Soil Type:")
    # Display soil options with ID and name
    for s in soils:
        print(f"{s.id}: {s.name}")
    # Ask user to select soil type by ID
    soil_id = int(input("Soil Type ID: "))

    # Fetch all regions from the database
    regions = session.query(Region).all()
    print("Select Region:")
    # Display region options with ID and name
    for r in regions:
        print(f"{r.id}: {r.name}")
    # Ask user to select region by ID
    region_id = int(input("Region ID: "))

    # Create a new Watershed object using the selected options
    ws = Watershed(
        name=name,
        area_hectares=area,
        land_use_id=land_use_id,
        soil_id=soil_id,
        region_id=region_id
    )

    # Add the new watershed to the session
    session.add(ws)
    # Commit the changes to save it in the database
    session.commit()

    # Print a confirmation message with the new watershed ID
    print(f"Watershed '{ws.name}' added with ID {ws.id}.")

    # Close the database session
    session.close()