# from email import message
import json
import string
from wsgiref import headers

import requests
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from twilio.twiml.messaging_response import (Body, Message, MessagingResponse,
                                             Redirect)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC43ef78c7eeaed4a7946b247ece883c71'
auth_token = 'd9ea1e96a8bc3e4e72f737d960c8c738'
client = Client(account_sid, auth_token)


auth="Token 76e3102018abefd92b167d04b352a775780134020116739c8022b330e0c2717a"
sent="urn:uuid:475fc14c-b95d-4bd3-a33d-7dfada5ca0a0"

@csrf_exempt
def bot(request):
    sender_message = request.POST["Body"],
    sender_number = request.POST["From"]

    url = "http://0.0.0.0:8008/js/walker_run"

    payload = json.dumps({
        "name": "talker",
        "ctx": {
            "question": sender_message[0], 
            "phone_number":sender_number
            },
        "_req_ctx": {},
        "snt": sent,
        "profiling": False,
        "is_async": False
    })
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    return HttpResponse(response)




