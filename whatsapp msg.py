import os
import pywhatkit
import time

"""
a = 0
phone_number = ['+91 8148688130', '+91 9150164513']
# min=int(input("enter the sec: "))
d = 0
while a < len(phone_number):
    pywhatkit.sendwhats_image(phone_no=phone_number[d], img_path="datascience.png",
                          caption="This is pps whatsapp marketing", wait_time=30)
    d += 1
    a += 1
"""

"""
pywhatkit.sendwhats_image(phone_no='+918148688130',
                          img_path="datascience.png",
                          caption="This is pps whatsapp marketing", wait_time=15)
"""


# pywhatkit.image_to_ascii_art("E:\papa\IMG_2948.JPG", "pywhat.txt")

"""
a = 0
phone_number = ['+91 8148688130', '+91 9150164513']
d = 0
def whatsapp_auto():
    pywhatkit.sendwhats_image(phone_no=phone_number[d], img_path="datascience.png",
                              caption="This is pps whatsapp marketing", wait_time=30)


while a < len(phone_number):
    time.sleep(10)
    whatsapp_auto()
    time.sleep(10)
    d += 1
    a += 1
"""

print(pywhatkit.info("virat kohli", lines=100))

