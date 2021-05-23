from bs4 import BeautifulSoup
import requests
import smtplib
import os
import lxml

# TODO: Use the requests library to request the HTML page of the Amazon product using the URL you got.
target_price = 200.00
product_url = "https://www.amazon.com/All-new-Kindle-Oasis-now-with-adjustable-warm-light/dp/B07GRSK3HC/ref=sr_1_3?dchild=1&keywords=kindle&qid=1621797329&sr=8-3&th=1"
http_header = {
    "accept_language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
response = requests.get(product_url, headers=http_header)
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")
product_title = soup.find(name="title").getText().split(":")[1]
price = float(soup.find(name="span", id="priceblock_ourprice").getText().split("$")[1])
message = f"Subject:Amazon Price Alert for {product_title}! \n\n{product_title} is now ${price}.\n\nSee more: {product_url}"
print(f"Product Title: {product_title}")
print(f"Price of the product: ${price}")

# TODO: We want to get an email when the price of our product is below a certain value.
# If the price is lower than the target price, then email me
if price < target_price:
    # ***WARNING***: Make sure you use a dummy email account to test this out!
    my_email = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    with smtplib.SMTP(os.getenv("SMTP"), port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        # Write messages
        connection.sendmail(
            from_addr=my_email,
            to_addrs="contact@byoungjun.com",
            msg=message.encode('ascii', 'ignore')
        )