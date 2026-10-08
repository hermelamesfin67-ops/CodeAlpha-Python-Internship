import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url
try:
    response = requests.get(url)
    response.raise_for_status
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.text
    with open("title.text", "w")as file:
        file.write(title)
    print("Title saved successfully!")
except requests.exceptions.RequestException as e:
    print("Error:", e)
    