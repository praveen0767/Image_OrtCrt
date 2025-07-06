Image Background Removal and Orientation Correction
This project provides a Python script that:

Removes the background from an input image using the rembg library.
Generates 360 rotated versions (0° to 359°) of the background-removed image.
Trains a Convolutional Neural Network (CNN) to predict the rotation angle of an image.
Corrects the orientation of a wrongly oriented image to either 0° or 359° using the trained CNN.

The script is designed to run on Windows with Python 3.13, though it may work with other versions (3.9–3.12 recommended for TensorFlow compatibility). All outputs are saved in the project directory.
Prerequisites
Software

Python 3.13 (or 3.9–3.12 for better TensorFlow compatibility)
pip (Python package manager)

Dependencies
Install the required libraries using:
pip install rembg==2.0.59 pillow==10.4.0 tensorflow==2.17.0 numpy==1.26.4

Input Files

Input Image: An image (e.g., input.jpg) for background removal, placed in C:\Users\prave\image_ai1.
Test Image: A wrongly oriented PNG image with a transparent background (e.g., wrongly_oriented.png), similar to the background-removed image, placed in C:\Users\prave\image_ai1.

Project Structure
C:\Users\prave\image_ai1\
├── input.jpg                   # Input image for background removal
├── wrongly_oriented.png        # Test image for orientation correction
├── bg_remove_and_correct.py    # Main script
├── output_bg_removed.png       # Background-removed image (output)
├── corrected_image.png         # Corrected orientation image (output)
├── orientation_cnn_model.h5    # Trained CNN model (output)
├── rotated_images\             # Folder for 360 rotated images (output)
│   ├── rotated_000.png
│   ├── rotated_001.png
│   ├── ...
│   └── rotated_359.png
└── README.md                   # This file

Setup

Install Python 3.13:

Download and install Python 3.13 from python.org.
Ensure pip is available and points to Python 3.13:C:/Users/prave/AppData/Local/Programs/Python/Python313/Scripts/pip.exe --version




Install Dependencies:Run the following command in the Command Prompt or PowerShell:
pip install rembg==2.0.59 pillow==10.4.0 tensorflow==2.17.0 numpy==1.26.4


Prepare Input Files:

Place input.jpg (or your input image) in C:\Users\prave\image_ai1.
Place wrongly_oriented.png (a rotated version of the background-removed image) in C:\Users\prave\image_ai1.


Optional: Use a Virtual Environment:To avoid package conflicts, create a virtual environment:
cd C:\Users\prave\image_ai1
python -m venv venv
.\venv\Scripts\activate
pip install rembg==2.0.59 pillow==10.4.0 tensorflow==2.17.0 numpy==1.26.4



Usage

Save the Script:

Save the provided bg_remove_and_correct.py script in C:\Users\prave\image_ai1.


Run the Script:

Open a Command Prompt or PowerShell.
Navigate to the project directory:cd C:\Users\prave\image_ai1


Execute the script:C:/Users/prave/AppData/Local/Programs/Python/Python313/python.exe bg_remove_and_correct.py




Script Workflow:

Background Removal: Removes the background from input.jpg and saves it as output_bg_removed.png.
Rotation Generation: Creates 360 rotated images (rotated_000.png to rotated_359.png) in rotated_images.
CNN Training: Trains a CNN model on the rotated images to predict rotation angles and saves it as orientation_cnn_model.h5.
Orientation Correction: Corrects the orientation of wrongly_oriented.png to 0° or 359° and saves it as corrected_image.png.



Outputs

output_bg_removed.png: Background-removed image (PNG with transparency).
rotated_images/: Folder containing 360 rotated images (rotated_000.png to rotated_359.png).
orientation_cnn_model.h5: Trained CNN model for orientation prediction.
corrected_image.png: Corrected test image, rotated to 0° or 359°.

Notes

Python 3.13 Compatibility: TensorFlow 2.17.0 is optimized for Python 3.9–3.12. If you encounter issues, use Python 3.12:python3.12 -m venv venv
.\venv\Scripts\activate
pip install rembg==2.0.59 pillow==10.4.0 tensorflow==2.17.0 numpy==1.26.4


Test Image: Ensure wrongly_oriented.png is a PNG with a transparent background and similar content to output_bg_removed.png for accurate CNN predictions.
Performance: The script uses 128x128 images for efficiency. Adjust img_size in the script for higher resolution, but this increases memory and training time.
Disk Space: Ensure ~360MB of free disk space for the 360 rotated images and sufficient RAM (4GB recommended) for CNN training.

Troubleshooting

ModuleNotFoundError:
Verify all dependencies are installed:pip list | findstr "rembg pillow tensorflow numpy"


Ensure pip and python point to the same environment:where python
where pip




File Not Found:
Confirm input.jpg and wrongly_oriented.png are in C:\Users\prave\image_ai1.
Check that rotated_images contains all 360 images after the rotation step.


CNN Accuracy:
If orientation correction is inaccurate, increase epochs (e.g., to 20) in the script or ensure the test image matches the training data.


TensorFlow Issues:
If TensorFlow fails on Python 3.13, try a pre-release version:pip install tf-nightly





License
This project is for personal use and provided as-is. Ensure you have the necessary licenses for the input images and libraries used.
Contact
For issues or questions, please provide error messages and details about your setup (e.g., Python version, input image characteristics).