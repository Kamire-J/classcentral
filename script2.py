from google.cloud import translate_v2 as translate
from bs4 import BeautifulSoup
import os

# Create a translate client
translate_client = translate.Client()

# Folder paths
input_folder = "www.classcentral.com"
output_folder = "output"


# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Set the source and target languages
source_language = 'en'
target_language = 'hi'

# Load the HTML file
for filename in os.listdir(input_folder):
    if filename.endswith('.html'):
        with open('index.html', 'r') as f:
            html = f.read()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Translate each text node in the HTML
        for text_node in soup.find_all(text=True):
            if text_node.parent.name in ['script', 'style']:
                # Skip script and style tags
                continue
            translated_text = translate_client.translate(text_node.string, source_language=source_language, target_language=target_language)
            text_node.string.replace_with(translated_text['translatedText'])

        # Save the translated HTML to a new file
        # Save the translated HTML file to the output folder
        with open(os.path.join(output_folder, filename), 'w') as file:
            file.write(str(soup))
