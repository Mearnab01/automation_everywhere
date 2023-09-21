import requests
from PIL import Image
from io import BytesIO

url = "https://image.shutterstock.com/image-photo/full-hd-image-ladybird-on-260nw-1952398060.jpg"

try:
    # Send a GET request to fetch the image
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Access the content of the response
        image_content = response.content

        # Create an Image object from the response content
        image = Image.open(BytesIO(image_content))

        # Save the image to a file
        with open("img.jpg", "wb") as fp:
            fp.write(image_content)

        print("Image saved as 'img.jpg'.")
    else:
        print("Failed to retrieve the image. Status Code:", response.status_code)

except requests.RequestException as e:
    print("Error occurred:", e)
