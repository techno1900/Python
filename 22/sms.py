
from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

client.messages.create(
    from_='+16502906867',
    to='+94701869010',
    body="hello"
)