from PIL import Image
import os

def batch_resize(input_folder, output_folder, new_size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image
        img = Image.open(input_path)

        # Resize the image
        resized_img = img.resize(new_size)

        # Save the resized image
        resized_img.save(output_path)

# Example usage:
input_folder = "./spectrum"
output_folder = "./new_spectrum"
new_size = (224, 224)  # Set your desired width and height

batch_resize(input_folder, output_folder, new_size)