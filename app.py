from imports import *
from date import *


def get_emag_price(product_url, output_file='emag_price.txt'):
    # Send a GET request to the url
    response = requests.get(product_url)


    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Product elements
        price_element = soup.find('p', class_='product-new-price')
        name_element = soup.find('h1', class_='page-title')


        # Check if the element was found
        if price_element and name_element:
            price = price_element.text.strip()
            name = name_element.text.strip()

           # Save the price to the specified output file
            with open(output_file, 'a+') as file:
                file.write(f'{logdate} {name} {price} \n')

            print(f'The price of the product is: {price}. Price saved to {output_file}')
            asyncio.run(telegram_send.send(messages=[f'The price of the product is: {price}. Price saved to {output_file}']))
        else:
            print('Price element not found on the page.')
    else:
        print(f'Failed to fetch the page. Status code: {response.status_code}')

# Example usage
#product_url = input("Please enter emag product URL:")
example = "https://www.emag.ro/cos-de-gunoi-15-l-incorporabil-cu-capac-automat-gri-antracit-5618/pd/DC3L9QBBM/?ref=hdr-favorite_products"

get_emag_price(example)