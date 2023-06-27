import requests
import openai
from config import key


openai.api_key = key


# Image generator
def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size='256x256',
    )

    generated_image = response['data'][0]['url']
    return generated_image


# Downloads and saves image
def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)


# User enters texts then image is generated
prompt = input("Input your text:")
generated_image = generate_image(prompt)


# Save image url to into file
image_url = generated_image
save_path = 'image.jpg'
download_image(image_url, save_path)
