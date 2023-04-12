import os
from PIL import Image, ImageDraw, ImageFont

# Directory path where the pictures are located
directory = "C:/Users/Data Science/Desktop/Malwares"


input("Press any key to start")
# Loop through all the files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # Open the image
        image = Image.open(os.path.join(directory, filename))

        # Get the width and height of the image
        width, height = image.size

        # Create a drawing object
        draw = ImageDraw.Draw(image)

        # Define the font and size for the text
        font = ImageFont.truetype("arial.ttf", 16)

        # Define the text to be added
        text = " | Hassan Ashiq"

        # Calculate the size of the text
        text_width, text_height = draw.textsize(text, font)

        # Set the position for the text
        x = 40
        y = 990

        # Add the text to the image
        draw.text((x, y), text, fill="white", font=font)

        # Save the modified image
        image.save(os.path.join(directory, f"{filename}_with_name.png"))

print("Name added to all square pictures.")
input("Press any key to exit")
