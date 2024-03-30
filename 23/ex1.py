import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
question = soup.select(".s-post-summary")
print(question[0].attrs)

# print(question)

