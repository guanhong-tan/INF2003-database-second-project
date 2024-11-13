from datetime import datetime
# Status: "reserved", "completed", "canceled"
# This one for two different seats plans  ,333 and 224
{
  "_id": "booking_id_001",                     
  "user_id": "user_id_001",                     
  "event_id": "event_id_001",                  
  "status": "completed",                       
  "timestamp": "2024-11-15T10:00:00Z",         
  "total_price": 400,                           
  "qr_code": "https://example.com/qr/booking_id_001", 
  "expiration_time": "2024-11-15T10:15:00Z",    
  "seat_details": [                             
    {
      "seat_section_id": "seat_section_event_id_001_333", 
      "section": "333",
      "tickets_booked": 2,                      
      "price_per_ticket": 200,                  
      "color": "Periwinkle Blue",
      "color_code": "#9391f7",
      "capacity_limit": 100
    },
    {
      "seat_section_id": "seat_section_event_id_001_224", 
      "section": "224",
      "tickets_booked": 3,                      
      "price_per_ticket": 150,                  
      "color": "Peppermint Frosting",
      "color_code": "#b3f7ed",
      "capacity_limit": 100
    }
  ]
}

# This one for one seat plan , qr_code for now remove
{
  "_id": "booking_id_001",                     
  "user_id": "user_id_001",                     
  "event_id": "event_id_001",                  
  "status": "completed",                       
  "timestamp": "2024-11-15T10:00:00Z",         
  "total_price": 400,                           
  "qr_code": "https://example.com/qr/booking_id_001", 
  "expiration_time": "2024-11-15T10:15:00Z",    
  "seat_details": [                             
    {
      "seat_section_id": "seat_section_event_id_001_333", 
      "section": "333",
      "tickets_booked": 2,                      
      "price_per_ticket": 200,                  
      "color": "Periwinkle Blue",
      "color_code": "#9391f7",
      "capacity_limit": 100
    }
  ]
}