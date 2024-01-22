import requests
from bs4 import BeautifulSoup
import telegram_send
import asyncio

from date import * 

'''
def get_emag_price(product_url, output_file='emag_price.txt'):
    # Send a GET request to the url
    response = requests.get(product_url)
    logdate = date.today()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Price Element
        price_element = soup.find('p', class_='product-new-price')

        # Check if the element was found
        if price_element:
            price = price_element.text.strip()

           # Save the price to the specified output file
            with open(output_file, 'a+') as file:
                file.write(logdate + " " + price)

            print(f'The price of the product is: {price}. Price saved to {output_file}')
            asyncio.run(telegram_send.send(messages=[f'The price of the product is: {price}. Price saved to {output_file}']))
        else:
            print('Price element not found on the page.')
    else:
        print(f'Failed to fetch the page. Status code: {response.status_code}')

# Example usage
product_url = input("Please enter emag product URL:")
get_emag_price(product_url)

'''

print(logdate)