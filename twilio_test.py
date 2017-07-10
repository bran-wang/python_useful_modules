# coding: utf-8
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4a2c4e73723bb113999fb0a0f0ecbd74"
# Your Auth Token from twilio.com/console
auth_token  = "8b944fc702129b5a3abe777140131bfd"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+86134xxxxxxxx", 
    from_="+18289701692",
    body="Hello,----我是个机器人，请不要回复")

print(message.sid)
