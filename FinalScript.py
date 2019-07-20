import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Vegetal-Hair-Colour-Soft-Black/dp/B01I51ML8E/ref=sr_1_1_sspa?crid=DECMOM9XPN24&keywords=vegetal+hair+colour+soft+black&qid=1562049070&s=gateway&sprefix=vegetal+hair+color%2Caps%2C414&sr=8-1-spons&psc=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[1:7])
    
    if(converted_price < 700):
        send_mail()


    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('youremail@gmail.com','key of two step verification')
    
    subject = 'Vegetal Price Fell Down!'
    body = 'Buy it from here https://www.amazon.in/Vegetal-Hair-Colour-Soft-Black/dp/B01I51ML8E/ref=sr_1_1_sspa?crid=DECMOM9XPN24&keywords=vegetal+hair+colour+soft+black&qid=1562049070&s=gateway&sprefix=vegetal+hair+color%2Caps%2C414&sr=8-1-spons&psc=1'

    msg = ("Subject: {subject}\n\n {body}").format(subject=subject, body=body)
    
    server.sendmail(
       'youremail@gmail.com',
       'recieveremail@gmail.com',
       msg
    )    
    print('HEY, EMAIL HAS BEEN SENT!')
    server.quit()

check_price()
