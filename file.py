from bs4 import BeautifulSoup
from googletrans import Translator
import translators as ts

# Translator
translator = Translator(service_urls=["translate.google.com"])


html = open("index1.html", encoding="utf8").read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all(["p","ul","ol","h1","h2","h3","h4","h5","h6","td"])

for i in soup.findAll(tags):
   i.string.replace_with(ts.google(i.string,from_language='en', to_language='hi'))


with open("output.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))
