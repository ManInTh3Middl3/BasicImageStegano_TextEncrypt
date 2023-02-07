# Basic Image Steganography with Text Encryption.

#Prerequisites
 - Python Imaging Library (PIL)
 - PyCrypto library

To install the dependencies, you can use the following command:

    pip install pillow pycrypto

# Usage

To run the code, execute the following command:

    python hide_text_in_image.py <image_file> <text> [password]


 - The image_file parameter is the path to the image file you want to hide text in. 
 - The text parameter is the text you want to hide. 
 - The password parameter is an optional parameter that you can use to encrypt the text before hiding it in the image.

# Inputs and Outputs

 - The input to the code is the image file and the text you want to hide. 
 - The code outputs a new image file, named hidden_text.png, with the hidden text.

# Limitations

 - The current implementation of hiding text in an image is not secure, as the method used can easily be detected. 
 - This code should be used for educational or demonstration purposes only.
