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