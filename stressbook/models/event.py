from datetime import datetime
from db_connection import events_collection 
                       
sample_events = [{
    "_id": "event_id_001",
    "type": "Concert",
    "name": "Honkai Impact Music Fest 2024",
    "date": "2024-12-15T19:00:00Z",
    "location": "Singapore Indoor Stadium",
    "available_tickets": 12000,
    "reserved_tickets": 0,
    "sold_tickets": 0,
    "image_url": "static/images/concert_one.jpeg",
    "duration": "2 hours",
    "age_advisory": "General Audience",
    "description": "Experience the magical world of Honkai Impact through an orchestral performance featuring beloved tracks from the game.",
    "synopsis": "Join us for an unforgettable evening of music from Honkai Impact. The concert will feature a full orchestra performing iconic tracks from the game's soundtrack, accompanied by stunning visuals on the big screen.",
    "artist": "HOYO-MiX Symphony Orchestra",
    "organizer": "HoYoverse Entertainment",
    "terms_conditions": [
        "No photography or video recording allowed during the performance",
        "Late entry will only be permitted during suitable breaks",
        "No refunds or exchanges permitted"
    ],
    "faq": [
        {
            "question": "Is there a dress code?",
            "answer": "Smart casual is recommended"
        },
        {
            "question": "Are cameras allowed?",
            "answer": "No photography or recording devices are permitted during the show"
        }
    ],
    "highlights": [
        "Live orchestral performance",
        "HD screen projections",
        "Exclusive merchandise",
        "Meet & greet opportunities"
    ]
},

{
    "_id": "event_id_002",
    "type": "Concert",
    "name": "Genshin Impact Music Fest 2024",
    "date": "2024-12-18T19:00:00Z",
    "location": "Singapore Indoor Stadium",
    "available_tickets": 12000,
    "reserved_tickets": 0,
    "sold_tickets": 0,
    "image_url": "static/images/concert_two.jpeg",
    "duration": "2 hours",
    "age_advisory": "General Audience"
},
{
    "_id": "event_id_003",
    "type": "Concert", 
    "name": "Honkai Star Rail Music Fest 2024",
    "date": "2024-12-24T19:00:00Z",
    "location": "Singapore Indoor Stadium",
    "available_tickets": 12000,
    "reserved_tickets": 0,
    "sold_tickets": 0,
    "image_url": "static/images/concert_three.jpeg",
    "duration": "2 hours",
    "age_advisory": "General Audience"
}]

def create_events_onload():
    # Check if events already exist
    if events_collection.count_documents({}) == 0:
        events_collection.insert_many(sample_events)
        print("Sample events inserted into the database.")
    else:
        print("Events already initialized.")

def retrieve_events():
    return list(events_collection.find())

def get_event_by_id(event_id):
    print("Searching for event with ID:", event_id)  # Debug print
    print("Type of event_id:", type(event_id))      # Debug print
    
    # Find the event by its ID in the MongoDB collection
    event = events_collection.find_one({"_id": event_id})
    print("Found event:", event)                     # Debug print
    
    return event

def reset_events():
    events_collection.delete_many({})
    events_collection.insert_many(sample_events)
    
    # Verify the insertion
    count = events_collection.count_documents({})
    print(f"Database reset with {count} events")
    
    # Print all events to verify
    all_events = list(events_collection.find())
    for event in all_events:
        print(f"Event in DB: {event['_id']}")
