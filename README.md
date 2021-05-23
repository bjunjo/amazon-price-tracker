# Day 47: amazon-price-tracker
## Problem: Email alert me when the price of the product I want is lower than my target price
## Solutions
1. Use the `requests` library to request the HTML page of the Amazon product using the URL you got
```
target_price = 200.00
product_url = "Amazon URL of the Product You Want"

# You can see your http headers here: http://myhttpheader.com/
http_header = {
    "accept_language": "YOUR ACCEPT LANGUAGE",
    "user-agent": "YOUR USER AGENT"
}
response = requests.get(product_url, headers=http_header)
webpage = response.text
```
2. Parse the website using `BeautifulSoup`
```
soup = BeautifulSoup(webpage, "lxml")
product_title = soup.find(name="title").getText().split(":")[1]
price = float(soup.find(name="span", id="priceblock_ourprice").getText().split("$")[1])
message = f"Subject:Amazon Price Alert for {product_title}! \n\n{product_title} is now ${price}.\n\nSee more: {product_url}"
print(f"Product Title: {product_title}")
print(f"Price of the product: ${price}")
```
3. We want to get an email when the price of our product is below a certain value.
```
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
```
## Lessons
1. I love this feeling of using my `robot army` to do the work for me
