import requests
from bs4 import BeautifulSoup


def get_website_text(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            word_list = text.split()
            word_str = " ".join(word_list)
            return word_str
        else:
            print(f"Failed to retrieve website content. Status code: {response.status_code}")
            return response.status_code
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 404


