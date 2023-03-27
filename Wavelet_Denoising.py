import os
from skimage import io, restoration
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str, default='image.png', help='path to image')
opt = parser.parse_args()

# Set the image_files list based on whether the image argument is a directory or a file
if os.path.isdir(opt.image):
    image_files = [os.path.join(opt.image, f) for f in os.listdir(opt.image) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]
else:
    image_files = [opt.image]

# Loop over each image file and denoise it using BayesShrink
for image_file in image_files:
    # Load the image
    image = io.imread(image_file)

    # Apply BayesShrink denoising
    denoised_image = restoration.denoise_wavelet(image, method='BayesShrink')

    # Convert the denoised image from float64 to uint8
    denoised_image = (denoised_image * 255).astype('uint8')

    # Save the denoised image to the output directory with the same name
    output_file = os.path.join('test', os.path.basename(image_file))
    io.imsave(output_file, denoised_image)
