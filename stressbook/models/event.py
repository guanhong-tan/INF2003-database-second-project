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
    "image_url": "static/images/concert_one.jpeg"  
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
    "image_url": "static/images/concert_two.jpeg" 
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
    "image_url": "static/images/concert_three.jpeg"  
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
    # Find the event by its ID in the MongoDB collection
    print(events_collection.find_one({"_id": event_id}))
    return events_collection.find_one({"_id": event_id})
