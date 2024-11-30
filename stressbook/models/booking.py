from datetime import datetime
from db_connection import db

bookings_collection = db['bookings']

# Create indexes
def create_indexes():
    """Create indexes for the bookings collection"""
    # Index for querying bookings by user_id
    bookings_collection.create_index("user_id")
    
    # Compound index for querying by event_id and status
    bookings_collection.create_index([("event_id", 1), ("status", 1)])
    
    # Index for timestamp to optimize sorting by date
    bookings_collection.create_index("timestamp")

# Call create_indexes when initializing the application
create_indexes()

def create_booking(user_id, event_id, section, quantity, price_per_ticket, event_name, event_location):
    """Create a new booking record"""
    booking = {
        "user_id": user_id,
        "event_id": event_id,
        "status": "completed",
        "timestamp": datetime.now().isoformat(),
        "total_price": price_per_ticket * quantity,
        "seat_details": [{
            "section": section,
            "tickets_booked": quantity,
            "price_per_ticket": price_per_ticket
        }],
        "event_name": event_name,
        "event_location": event_location
    }
    
    return bookings_collection.insert_one(booking)

def get_user_bookings(user_id):
    """Get all bookings for a specific user"""
    try:
        return list(bookings_collection.find({"user_id": user_id}))
    except Exception as e:
        print(f"Error fetching user bookings: {str(e)}")
        return []