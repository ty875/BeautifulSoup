#download the image on local machine
import requests #pip install requests
from bs4 import BeautifulSoup as bs #pip install beautifulSoup4
import requests
import os

r = requests.get("https://ty875.github.io/BeautifulSoup/")
soup = bs(r.content, "html.parser")
url = "https://ty875.github.io/BeautifulSoup/"


image = soup.select("img")
image_url = image[0]['src']

#download it in the download folder
image_data = requests.get(image_url).content
download_folder = os.path.expanduser("~/Downloads")
image_path = os.path.join(download_folder, "Cat.jpg")

with open(image_path, 'wb') as handler:
    handler.write(image_data)
    
