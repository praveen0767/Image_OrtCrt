import os
import numpy as np
from PIL import Image
from rembg import remove
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import img_to_array
import warnings
warnings.filterwarnings("ignore", category=UserWarning) 

def remove_background(input_path, output_path):
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input image {input_path} not found.")
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path, "PNG")
        print(f"Background removed successfully! Output saved to {output_path}")
        return output_image
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred in background removal: {e}")
        return None

def create_rotated_images(input_path, output_folder, img_size=(128, 128)):
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
        print(f"An error occurred in rotation generation: {e}")

def load_training_data(image_folder, img_size=(128, 128)):
    images = []
    labels = []
    for angle in range(360):
        img_path = os.path.join(image_folder, f"rotated_{angle:03d}.png")
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Image {img_path} not found.")
        img = Image.open(img_path).convert("RGBA")
        img = img.resize(img_size)
        img_array = img_to_array(img) / 255.0
        images.append(img_array)
        labels.append(angle)
    return np.array(images), np.array(labels)

def build_cnn_model(input_shape):
    model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation="relu"),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation="relu"),
        Dropout(0.5),
        Dense(360, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

def train_cnn_model(image_folder, img_size=(128, 128), epochs=10):
    images, labels = load_training_data(image_folder, img_size)
    input_shape = (img_size[0], img_size[1], 4)
    model = build_cnn_model(input_shape)
    model.fit(images, labels, epochs=epochs, batch_size=32, verbose=1)
    model.save("orientation_cnn_model.h5")
    print("Model trained and saved as orientation_cnn_model.h5")
    return model

def correct_image_orientation(input_path, model, img_size=(128, 128)):
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input image {input_path} not found.")
        img = Image.open(input_path).convert("RGBA")
        img_resized = img.resize(img_size)
        img_array = img_to_array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_array, verbose=0)
        predicted_angle = np.argmax(prediction[0])
        correction_angle = 0 if abs(predicted_angle - 0) <= abs(predicted_angle - 359) else 359
        rotation_angle = (correction_angle - predicted_angle) % 360
        corrected_img = img.rotate(rotation_angle, expand=True, resample=Image.Resampling.BICUBIC)
        output_path = "corrected_image.png"
        corrected_img.save(output_path, "PNG")
        print(f"Corrected image saved to {output_path} (rotated by {rotation_angle}° to {correction_angle}°)")
        return corrected_img
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred in orientation correction: {e}")
        return None

if __name__ == "__main__":
    base_dir = "C:/Users/prave/image_ai1"
    input_image_path = os.path.join(base_dir, "image.png")  # Input image for background removal
    bg_removed_path = os.path.join(base_dir, "output_bg_removed.png")  # Output for background-removed image
    rotated_folder = os.path.join(base_dir, "rotated_images")  # Folder for rotated images
    test_image_path = r"C:/Users/prave/image_ai1/rotated_images/rotated_227.png"  # Input for orientation correction
    print("Starting background removal...")
    bg_removed_image = remove_background(input_image_path, bg_removed_path)
    if bg_removed_image is None:
        print("Background removal failed. Exiting.")
        exit(1)
    print("\nGenerating 360 rotated images...")
    create_rotated_images(bg_removed_path, rotated_folder)
    print("\nTraining CNN model...")
    model = train_cnn_model(rotated_folder, epochs=10)
    print("\nCorrecting orientation of test image...")
    corrected_image = correct_image_orientation(test_image_path, model)
    if corrected_image is None:
        print("Orientation correction failed.")
    else:
        print("Process completed successfully!")