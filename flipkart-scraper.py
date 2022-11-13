import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://dl.flipkart.com/s/FIpYZyuuuN"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
reviews = soup.find_all("div", {"class": "_2wzgFH"})
print(reviews)

# df = pd.DataFrame({"Reviewer": names of the reviewers})
# df["Reviews"] = df["A"].map(reviews variable)

# Due to encoding error I couldn't figure out how to scrape flipkart, and this code is correct as per my lund knowledge.
