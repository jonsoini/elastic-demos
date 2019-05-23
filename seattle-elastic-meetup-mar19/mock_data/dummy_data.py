# Script to fake data into Elastic (or anything really)
# Usues faker for lat/long bounding and other niceties so 'pip install faker' first
# To run it a bunch use something like 'watch -n 1 python dummy_data.py' (every 1s)

import json, requests, datetime, random
from faker import Faker
fake = Faker()

# Host for ES
host = "http://localhost:9200"
es_index = "dummy_app"

# Setup the fake facts

lat_long = fake.local_latlng(country_code="US", coords_only=True)

def convertTuple(tup): 
    str =  ', '.join(tup) 
    return str

fake_loc = convertTuple(lat_long)

fake_cust_id = fake.uuid4()

os_list = ['android','ios']
fake_model = random.choice(os_list)

number_clicks = random.randint(4,12)

def make_dummycustomer():
    return {
        'id': fake_cust_id,
        'location': fake_loc,
        'device_os': fake_model
    }

def make_dummyevent():
    fake_duration = random.randint(800, 2300)
    
    card_list = ['homeintrojan2019','account_summary','usage','welcome_card','more','contact_us','phone_promoABC','deals_today','line_details']
    fake_card = random.choice(card_list)

    event_list = ['card_view','card_click','card_render','card_expired']
    fake_eventtype = random.choice(event_list)

    # TODO make this UTC-friendly so one doesn't have to set timezone offset
    
    the_time = datetime.datetime.now().isoformat() + "-07:00"
    return {
      'duration_ms': fake_duration,
      'app_timestamp': the_time,
      'card_id': fake_card,
      'event_type': fake_eventtype
   }

customer = make_dummycustomer()

for x in range(number_clicks):
    dummy_payload = make_dummyevent()
    both = { 'customer' : customer, 'event' : dummy_payload }
    json.dumps(both,indent=2)

    headers = {'Content-Type': 'application/json'}
    response = requests.post(host + "/" + es_index + "/_doc/", json=both, headers=headers)

    print(both)
    print(response.status_code)
