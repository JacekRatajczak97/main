# https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events?hl=pl


import requests
import json
import time
import sys

api_secret = 'API_SECRET'
measurement_id = 'MEASUREMENT_ID'
client_id = '12345.67899'  # client ID _ga
timestamp_micros = int(time.time() * 1_000_000)
event_name = 'refund'


url = f'https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret={api_secret}'

payload = {
    "client_id": client_id,
    "timestamp_micros": timestamp_micros,
    "non_personalized_ads": False,
    "events": [
        {
            "name": event_name,
            "params": {
                "currency": "USD",
                "value": "9.99",
                "transaction_id": "ABC-123",
                "engagement_time_msec": 1200,
                "debug_mode": True
            }
        }
    ]
}

payload_json = json.dumps(payload)
payload_size_bytes = sys.getsizeof(payload_json)
payload_size_kb = payload_size_bytes / 1024

if(payload_size_kb < 130):

    # POST request
    response = requests.post(
            url, 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(payload)
        )

    # response
    if response.status_code == 204:
        print('Event sent successfully.')
    else:
        print(f'Error sending event: {response.status_code} - {response.text}')
else:
    print('Payload is to big')
