import os
import base64
from PIL import Image
from io import BytesIO

# Function to convert image to base64
def convert_image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffer = BytesIO()
        img.save(buffer, format="JPEG")  # Save the image to a buffer
        base64_string = base64.b64encode(buffer.getvalue()).decode('utf-8')  # Encode buffer to base64
    return base64_string


# Get the current working directory
current_directory = os.getcwd()


# Find all jpg files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(".jpg"):
        # Full file path
        file_path = os.path.join(current_directory, filename)
        
        # Convert image to base64
        base64_string = convert_image_to_base64(file_path)
        
        # New filename with "_base64" suffix
        new_filename = filename.rsplit(".", 1)[0] + "_base64.txt"
        new_file_path = os.path.join(current_directory, new_filename)
        
        # Save the base64 string to a new file
        with open(new_file_path, 'w') as base64_file:
            base64_file.write(base64_string)

        print(f"Base64 encoded file saved as: {new_filename}")
