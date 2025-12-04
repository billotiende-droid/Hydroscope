from app.db import SessionLocal
from app.models import Watershed, RainfallEvent, RunOffCalculation
from datetime import datetime

# Function to add a rainfall event to a specific watershed
def add_rainfall_event(watershed_id: int, rainfall_mm: float, date=None):
   # Create a new database session
   session = SessionLocal()

   # If no date is provided, use today's UTC date
   if date is None:
       date = datetime.utcnow().date()

   # Create a new RainfallEvent object with the provided data
   rainfall_event = RainfallEvent(
       watershed_id=watershed_id,
       rainfall_mm=rainfall_mm,
       date=date
   )

   # Add the new event to the database session
   session.add(rainfall_event)

   # Save (commit) the new rainfall event to the database
   session.commit()

   # Refresh the object so it contains updated data from the database (e.g., assigned ID)
   session.refresh(rainfall_event)

   # Close the database session
   session.close()

   # Return the created rainfall event object
   return rainfall_event

# Function to calculate runoff and store the result in the database
def calculate_runoff_linked(watershed_id: int, rainfall_mm: float, cn_used: int):
    # Create a new database session
    session = SessionLocal()

    # Record the rainfall event first and store it in the database
    # This returns a RainfallEvent object with an assigned ID
    rainfall = add_rainfall_event(watershed_id, rainfall_mm)

    # Fetch the watershed object using its ID
    ws = session.query(Watershed).get(watershed_id)

    # Compute S from Curve Number (SCS CN method formula)
    S = (1000 / cn_used) - 10

    # Calculate runoff depth (in mm) using the SCS runoff equation
    runoff_depth = max((rainfall_mm - 0.2 * S)**2 / (rainfall_mm + 0.8 * S), 0)

    # Convert runoff depth to total runoff volume:
    # area_hectares → convert to m² (multiply by 10,000)
    # depth(mm) → convert to meters (divide by 1000)
    # Then compute volume (m³)
    runoff_volume = runoff_depth * ws.area_hectares * 10000 / 1e6  # m³

    # Create a new RunOffCalculation record
    runoff = RunOffCalculation(
        watershed_id=watershed_id,
        rainfall_id=rainfall.id,
        cn_used=cn_used,
        run_off_depth_mm=runoff_depth,
        run_off_volume=runoff_volume,
        time_stamp=datetime.utcnow()
    )

    # Add the runoff calculation to the session
    session.add(runoff)

    # Save it to the database
    session.commit()

    # Refresh the object to include database-generated values (e.g., ID)
    session.refresh(runoff)

    # Close the session
    session.close()

    # Return the created RunOffCalculation object
    return runoff


    