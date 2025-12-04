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
