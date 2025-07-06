import tensorflow as tf
from PIL import Image
import os
import numpy as np

def correct_orientation(model_path, wrong_image_path, output_path):
    try:
        model = tf.keras.models.load_model(model_path, compile=True)
        img = Image.open(wrong_image_path).convert('RGB')
        img.thumbnail((1024, 1024), Image.LANCZOS)
        img = img.resize((256, 256), Image.LANCZOS)
        img_array = np.array(img) / 255.0
        angle = model.predict(img_array[np.newaxis, ...])[0][0]
        print(f"Predicted angle: {angle:.1f}°")
        corrected_angle = -(angle % 360)
        corrected = img.rotate(corrected_angle, expand=True)
        corrected = corrected.crop(corrected.getbbox())
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        corrected.save(output_path, 'PNG', quality=95)
        final_angle = (360 - (angle % 360)) % 360
        print(f"Corrected by {corrected_angle:.1f}° -> {output_path}")
        print(f"Final image orientation: {final_angle:.1f}°")
    except Exception as e:
        print(f"Error in correct_orientation: {e}")

if __name__ == "__main__":
    try:
        model_path = r"C:\Users\prave\image_ai\image_orientation_correction\final_img\orientation_corrector.h5"
        wrong_image_path = r"C:\Users\prave\image_ai\image_orientation_correction\rotated_images_test\rotated_200.png"
        output_path = r"C:\Users\prave\image_ai\image_orientation_correction\final_img\corrected_image.png"
        print("Correcting test image orientation...")
        correct_orientation(model_path, wrong_image_path, output_path)
    except Exception as e:
        print(f"Error in main block: {e}")