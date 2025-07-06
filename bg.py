from rembg import remove
from PIL import Image
import os

def remove_background(input_path, output_path):
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input image {input_path} not found.")
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path, "PNG")
        print(f"Background removed successfully! Output saved to {output_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    input_image_path =r"C:/Users/prave/image_ai1/image.png"  
    output_image_path = "output_bg_removed.png"  
    remove_background(input_image_path, output_image_path)