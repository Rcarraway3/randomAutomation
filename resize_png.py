from PIL import Image
import os
import glob # For finding files based on a pattern

def scale_png_uniformly(input_path: str, output_size: tuple = (250, 250), output_suffix: str = "_scaled") -> str:
    """
    Scales a PNG image uniformly to the specified output size.
    The image is resized to fit within the output_size while maintaining its aspect ratio,
    and then centered on a transparent canvas of the specified output_size.

    Args:
        input_path (str): The path to the input PNG file.
        output_size (tuple): A tuple (width, height) for the desired output dimensions.
                             Defaults to (250, 250).
        output_suffix (str): Suffix to add to the output filename before the extension.
                             Defaults to "_scaled".

    Returns:
        str: The path to the newly created scaled image file, or an empty string if an error occurred.
    """
    if not os.path.exists(input_path):
        print(f"Error: Input file not found at '{input_path}'")
        return ""

    try:
        img = Image.open(input_path)
        img.load() # Ensures image data is loaded into memory before processing

        # Convert to RGBA if not already (important for PNG transparency)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # Use thumbnail to resize the image while maintaining aspect ratio,
        # ensuring it fits within the output_size.
        # Image.Resampling.LANCZOS is a high-quality downsampling filter.
        img.thumbnail(output_size, Image.Resampling.LANCZOS)

        # Create a new blank image with the desired output_size and fill with transparency.
        # This new image will be the final output canvas.
        new_img = Image.new('RGBA', output_size, (255, 255, 255, 0)) # Fully transparent background
        
        # Calculate paste position to center the thumbnail on the new_img canvas.
        paste_x = (output_size[0] - img.width) // 2
        paste_y = (output_size[1] - img.height) // 2
        
        # Paste the resized image onto the transparent canvas.
        new_img.paste(img, (paste_x, paste_y))

        # Construct the output filename by adding the suffix before the original extension.
        base_name, ext = os.path.splitext(input_path)
        output_path = f"{base_name}{output_suffix}{ext}"

        # Save the new scaled image.
        new_img.save(output_path)
        print(f"Successfully scaled '{input_path}' to '{output_path}' ({output_size[0]}x{output_size[1]}px).")
        return output_path

    except Exception as e:
        print(f"An error occurred while processing '{input_path}': {e}")
        return ""

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Prompt user for desired output size
    print("Enter the desired output dimensions for your PNG files.")
    try:
        width = int(input("Enter target width (e.g., 250): "))
        height = int(input("Enter target height (e.g., 250): "))
        output_dims = (width, height)
    except ValueError:
        print("Invalid input. Please enter integers for width and height.")
        exit() # Exit if input is not valid

    print(f"\nScanning for PNG files in: {script_dir}")
    
    # Find all PNG files in the script's directory
    # Using glob.glob for pattern matching
    png_files = glob.glob(os.path.join(script_dir, "*.png"))

    if not png_files:
        print(f"No PNG files found in '{script_dir}'.")
    else:
        print(f"Found {len(png_files)} PNG file(s). Processing...")
        for png_file in png_files:
            scale_png_uniformly(png_file, output_size=output_dims)
        print("\nAll specified PNG files processed.")

