# import requests
# from bs4 import BeautifulSoup
# import os
#
# # Set the website URL
# base_url = "https://sites.google.com/view/dr-a-halder/subjects"  # Change to your professor's website
# page = requests.get(base_url)
#
# # Parse HTML
# soup = BeautifulSoup(page.content, "html.parser")
#
# # Find all PPT links
# ppt_links = []
# for link in soup.find_all("a", href=True):
#     if link["href"].endswith((".ppt", ".pptx")):
#         ppt_links.append(base_url + link["href"])
#
# # Create a folder to save PPTs
# os.makedirs("PPT_Files", exist_ok=True)
#
# # Download PPT files
# for ppt_url in ppt_links:
#     file_name = ppt_url.split("/")[-1]
#     file_path = os.path.join("PPT_Files", file_name)
#
#     response = requests.get(ppt_url)
#     with open(file_path, "wb") as file:
#         file.write(response.content)
#
#     print(f"Downloaded: {file_name}")
import pandas as pd
from tabulate import tabulate

df = pd.read_csv('aug_train.csv')
print(tabulate(df.sample(15),headers='keys',tablefmt='simple'))
