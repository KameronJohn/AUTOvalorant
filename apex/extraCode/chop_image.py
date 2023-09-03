from PIL import Image

def separate_image(image_path,filename):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB mode
    image = image.convert('RGB')

    # Get the width and height of the image
    width, height = image.size

    # Calculate the split point
    split_point = int(height * 0.75)

    # Separate the image into two parts
    top_part = image.crop((0, 0, width, split_point))
    bottom_part = image.crop((0, split_point, width, height))

    # Save the top part
    top_part.save(r'C:\Users\User\Documents\GitHub\inGameSelection\apex\apex_source\legends\soft'+"\\"+filename)

    # Save the bottom part
    bottom_part.save(r'C:\Users\User\Documents\GitHub\inGameSelection\apex\apex_source\legends\hard'+"\\"+filename)
    print(f"Done: {image_path}")
# Example usage
# image_path = r'C:\Users\User\Documents\GitHub\inGameSelection\apex\apex_source\2023-07-24_00-07-11_gibraltar(support) is picked.png'
# separate_image(image_path)
import os

def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_path_name = os.path.join(directory, filename)
            separate_image(file_path_name,filename)
def main():
    # Example usage
    directory_path = r'C:\Users\User\Documents\GitHub\inGameSelection\apex\apex_source\legends\available'
    process_files_in_directory(directory_path)
if __name__ == '__main__':
    main()