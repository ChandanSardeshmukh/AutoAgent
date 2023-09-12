import requests
from bs4 import BeautifulSoup

# Define a list of websites to scrape for airfares
websites = [
    {
        'name': 'Website 1',
        'url': 'https://www.website1.com/airfares',
    },
    {
        'name': 'Website 2',
        'url': 'https://www.website2.com/airfares',
    },
    # Add more websites as needed
]

def scrape_airfares(website):
    try:
        # Send an HTTP GET request to the website
        response = requests.get(website['url'])
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract relevant information such as prices, airlines, and dates
        # Adjust the following code to match the specific structure of each website
        prices = soup.find_all('span', class_='fare-price')
        airlines = soup.find_all('div', class_='airline')
        dates = soup.find_all('div', class_='flight-date')

        # Process and store the data as needed
        for i in range(len(prices)):
            price = prices[i].text.strip()
            airline = airlines[i].text.strip()
            date = dates[i].text.strip()
            
            # You can save or process this data in your preferred way
            print(f"{website['name']} - {date}: {airline} - {price}")

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {website['name']}: {e}")
    except Exception as e:
        print(f"An error occurred while processing {website['name']}: {e}")

def main():
    for website in websites:
        scrape_airfares(website)

if __name__ == "__main__":
    main()
