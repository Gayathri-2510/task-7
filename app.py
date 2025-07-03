import os
from PIL import Image

input_folder = './input_images'
output_folder = './output_images'
resize_dimensions = (800, 600)  
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

for filename in os.listdir(input_folder):
    if filename.lower().endswith(image_extensions):
        input_path = os.path.join(input_folder, filename)
        try:
            with Image.open(input_path) as img:
                img_resized = img.resize(resize_dimensions, Image.Resampling.LANCZOS)
                base_name, ext = os.path.splitext(filename)
                new_filename = f"{base_name}_resized.jpg"
                output_path = os.path.join(output_folder, new_filename)
                img_resized.convert('RGB').save(output_path, 'JPEG')
                print(f"Resized and saved: {new_filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
