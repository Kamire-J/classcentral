from googletrans import Translator
from bs4 import BeautifulSoup
import os

# Translator
translator = Translator(service_urls=["translate.google.com"])


# Folder paths
input_folder = "www.classcentral.com"
output_folder = "output"


# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.html'):
        # Read in the HTML file
        with open(os.path.join(input_folder, filename), 'r') as file:
            html = file.read()

        # Extract the text content from the HTML file using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all(["p","ul","ol","h1","h2","h3","h4","h5","h6","td"])
        text = soup.get_text()

        # Translate the text content using the translator
        translated_text = translator.translate(text, dest='hi').text

        # Replace the text content in the HTML file with the translated text
        soup.body.string = translated_text

        # Save the translated HTML file to the output folder
        with open(os.path.join(output_folder, filename), 'w') as file:
            file.write(str(soup))