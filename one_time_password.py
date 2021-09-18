import random
from twilio.rest import Client

otp = random.randint(1000, 9999)
print(otp)
account_sid = 'ACcf28d2ae71d6570cbbfb59a94c1245b0'
auth_token = 'ddc6c2f59556315e4fa6cba7c52f7ba6'
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    body='Your OTP is-'+str(otp),
    from_='9176528966',
    to='+918148688130'
)

print(message.sid)



