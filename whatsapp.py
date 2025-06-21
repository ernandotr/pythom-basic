import pywhatkit as kit
import datetime

now = datetime.datetime.now()

phone_number = "+351934999999"  # Replace with the recipient's phone number

message = ("Hello, this is a test message sent using pywhatkit!")

kit.sendwhatmsg(phone_number, message, now.hour, now.minute + 1)
print("Message sent successfully.")