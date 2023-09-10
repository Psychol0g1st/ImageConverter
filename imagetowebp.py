# import os
# from PIL import Image

# def convert_to_webp(input_path, output_folder, quality=80):
#     try:
#         # Create the output folder if it doesn't exist
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         # List all image files in the input folder
#         image_files = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
#         image_files = [f for f in image_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

#         for image_file in image_files:
#             input_image_path = os.path.join(input_path, image_file)
#             output_webp_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + ".webp")

#             # Open the input image
#             with Image.open(input_image_path) as img:
#                 # Convert the image to RGBA mode if it has an alpha channel
#                 if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
#                     img = img.convert('RGBA')
#                 else:
#                     img = img.convert('RGB')
                
#                 # Convert the image to WebP format
#                 img.save(output_webp_path, "webp", quality=quality)
#             print(f"Image converted to WebP and saved to: {output_webp_path}")
#     except Exception as e:
#         print(f"Error converting images: {str(e)}")

# if __name__ == "__main__":
#     input_folder = "input"  # Replace with the path to your input image folder
#     output_folder = "output"  # Replace with the desired output folder

#     convert_to_webp(input_folder, output_folder, quality=80)



import os
from PIL import Image

def convert_to_webp(input_path, output_folder, quality=80):
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for root, _, files in os.walk(input_path):
            # Get the relative path to the subfolder from the input folder
            rel_path = os.path.relpath(root, input_path)
            output_subfolder = os.path.join(output_folder, rel_path)

            # Create the subfolder in the output directory if it doesn't exist
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)

            # List all image files in the current subfolder
            image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

            for image_file in image_files:
                input_image_path = os.path.join(root, image_file)
                output_webp_path = os.path.join(output_subfolder, os.path.splitext(image_file)[0] + ".webp")

                # Open the input image
                with Image.open(input_image_path) as img:
                    # Convert the image to RGBA mode if it has an alpha channel
                    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                        img = img.convert('RGBA')
                    else:
                        img = img.convert('RGB')

                    # Convert the image to WebP format
                    img.save(output_webp_path, "webp", quality=quality)
                print(f"Image converted to WebP and saved to: {output_webp_path}")
    except Exception as e:
        print(f"Error converting images: {str(e)}")

if __name__ == "__main__":
    input_folder = "input"  # Replace with the path to your input image folder
    output_folder = "output"  # Replace with the desired output folder

    convert_to_webp(input_folder, output_folder, quality=80)
