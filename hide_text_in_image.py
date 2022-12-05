from PIL import Image, ImageDraw
from Crypto.Cipher import AES
import random

def hide_text_in_image(image_file, text, password=None):
    # Load the image
    image = Image.open(image_file)
    grayscale_image = image.convert("L")
    draw = ImageDraw.Draw(grayscale_image)

    # Encrypt the text using the password (if provided)
    if password:
        cipher = AES.new(password)
        encrypted_text = cipher.encrypt(text)
        text = encrypted_text

    # Hide the text in the image
    x = random.randint(0, image.width - 1)
    y = random.randint(0, image.height - 1)
    draw.text((x, y), text)

    # Save the image with the hidden text
    new_image_file = "hidden_text.png"
    grayscale_image.save(new_image_file)
