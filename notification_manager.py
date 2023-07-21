import smtplib

import requests
SHEETY_API = "https://api.sheety.co/8733df2434363dff6967d520106ad4a2/copyOfFlightDeals/users"

# from twilio.rest import Client
# account_sid = 'ACf550b400ec77e3ee5d0eea84e945bcf3'
# auth_token = '3b1896a7737309b846888bdf2e29ec04'
# client = Client(account_sid, auth_token)
class NotificationManager:
    def send_sms(self, offers):
        response = requests.get(url= SHEETY_API)
        response = response.json()
        users = response["users"]
        s = smtplib.SMTP('smtp.gmail.com')
        s.starttls()
        s.login("sharmakrishnaroyalacademy@gmail.com", "xepzaxywpigeehqy")
        for user in users:
            for offer in offers:
                body = f"\nFlight to {offer['cityTo']} at {offer['price'] * 92.18} Rs\n" \
                       f"Airlines: {offer['airlines'][0]}\n" \
                       f"{offer['deep_link']}"

                message = f"Subject: CHEAP FLIGHT ALERT \n\n {body}"
                s.sendmail("sharmakrishnaroyalacademy@gmail.com", user["email"], message)

                # message = client.messages.create(
                #     body=f"\nFlight to {offer['cityTo']} at {offer['price']*92.18} Rs\n"
                #          f"Airlines: {offer['airlines']}\n"
                #          f"{offer['deep_link']}",
                #     from_='+12343199779',
                #     to='+919175095845'
                # )
                # print(message.sid)



