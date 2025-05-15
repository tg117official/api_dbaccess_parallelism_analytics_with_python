from PIL import Image
import numpy as np
import os

def increase_brightness(input_path, output_path, brightness_factor=30):
    # Step 1: Open the image
    image = Image.open(input_path).convert('RGB')

    # Step 2: Convert to NumPy array
    image_array = np.array(image)

    # Step 3: Increase brightness (clipping at 255 to avoid overflow)
    brighter_array = np.clip(image_array + brightness_factor, 0, 255).astype(np.uint8)

    # Step 4: Convert back to Image
    brighter_image = Image.fromarray(brighter_array)

    # Step 5: Save the new image
    brighter_image.save(output_path)
    print(f"Image saved to {output_path}")

# Example usage
if __name__ == "__main__":
    input_image_path = r"C:\Users\Sandeep\Pictures\sample.jpg"           # Replace with your input image path
    output_image_path = r"C:\Users\Sandeep\Pictures\brighter_sample.jpg" # Output image path

    if os.path.exists(input_image_path):
        increase_brightness(input_image_path, output_image_path, brightness_factor=90)
    else:
        print(f"Input file {input_image_path} does not exist.")
