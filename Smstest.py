from twilio.rest import TwilioRestClient

account = "ACa23a4631f480400ab4bb097413e1385e"
token = "f534e790f21f96f11087a50df5fc92ea"
client = TwilioRestClient(account, token)

message = client.sms.messages.create(to="+15712511409", from_="+14155992671",
                                     body="fuck ya :D")
print message