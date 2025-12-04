from app.db import init_db

def main():
    # Initialize the database tables 
    init_db()
    print("HydroScope database initialized successfully.")

if __name__ == "__main__":
    main()
