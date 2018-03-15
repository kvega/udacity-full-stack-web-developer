from twilio.rest import Client

# Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.sms.messages.create(body="Hello, world!",
	to="+18005551234",
	from_="+18005554321")

print(message.sid)