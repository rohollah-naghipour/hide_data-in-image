from stegano import lsb
from PIL import Image

image_path = input("Enter your image path: ")
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print("Error: File not found")
    exit()

secret = lsb.hide(image_path, "This is a secret text")
secret.save("image-secret.png")

clear_message = lsb.reveal("image-secret.png")
print("Hidden text:", clear_message)
