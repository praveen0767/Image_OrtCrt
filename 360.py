from PIL import Image
import os

def create_rotated_images(input_path, output_folder):
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input image {input_path} not found.")

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Created output folder: {output_folder}")
        input_image = Image.open(input_path)
        if input_image.mode != 'RGBA':
            input_image = input_image.convert('RGBA')
            print("Converted image to RGBA for transparency.")
        for angle in range(360):
            rotated_image = input_image.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
            output_path = os.path.join(output_folder, f"rotated_{angle:03d}.png")
            rotated_image.save(output_path, "PNG")
            print(f"Saved rotated image at angle {angle}° to {output_path}")

        print(f"Successfully generated 360 rotated images in {output_folder}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_image_path = "output_bg_removed.png" 
    output_folder_path = "rotated_images"      
    create_rotated_images(input_image_path, output_folder_path)