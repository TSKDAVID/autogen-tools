import requests
from openai import OpenAI

def generate_and_download_image(prompt, style="vivid", size="1024x1024", filename="generated_image.png"):
    # initialize the OpenAI client
    client = OpenAI()
    
    # generate the image
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size=size,
        style=style
    )
    
    # extract the image URL from the response
    image_url = response['data'][0]['url']
    
    # download the image
    image_data = requests.get(image_url).content
    
    # save the image to a file
    with open(filename, 'wb') as file:
        file.write(image_data)
    
    return(f"Image downloaded and saved as {filename}")

# this code generates and download the image from openai's dalle 3 model, it receives 4 arguments and you could remove any of them and just set them manually if you dont want it, make sure to describe this tool to the agent
# well so that it know what arguments to provide and what to expect
