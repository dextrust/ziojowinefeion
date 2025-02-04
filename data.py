import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Parse the data you need from the website
        # This is an example and should be modified based on the website's structure
        data = soup.find_all('div', class_='economic-data')
        return data
    else:
        print(f"Failed to retrieve data from {url}")
        return []

def get_all_data():
    urls = [
        'https://www.investing.com/economic-calendar/'
        # Add more URLs as needed
    ]
    all_data = []
    for url in urls:
        data = scrape_website(url)
        all_data.extend(data)
    return all_data

if __name__ == "__main__":
    data = get_all_data()
    # Save data to a file or prepare it for summarizer.py
    with open('economic_data.txt', 'w') as file:
        for item in data:
            file.write(f"{item}\n")