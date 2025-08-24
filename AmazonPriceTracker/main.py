import os
import smtplib
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
email = os.getenv("Email")
password = os.getenv("Password")
email2 = os.getenv("Email2")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
          "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
          }
url ="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(url = url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
data= soup.find(name="span" , class_="a-price-whole")
price_text = data.getText()

price = price_text.replace(".","").split(".")[0]
price_as_float = float(price)

if price_as_float > 100:
    pass
else:
    with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
        connection.starttls()
        result = connection.login(email2 , password)
        connection.sendmail(
            from_addr= email2,
            to_addrs= email,
            msg= f"Subject: Amazon Price Alert!!!\n\n"
                 f"The instant pot is below $100. It is {price_as_float}$"
        )

