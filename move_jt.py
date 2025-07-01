import os
import shutil

def move_jt_files():
    # Get the directory the script is located in
    root_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Walk through the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Check if the current directory is the root directory
        if dirpath == root_dir:
            continue  # Skip the root directory itself, as we don't want to move files from here
        
        # Iterate over all files in the directory
        for filename in filenames:
            # If the file ends with '.jt'
            if filename.endswith('.jt'):
                # Full path to the file
                file_path = os.path.join(dirpath, filename)
                
                # Destination path in the root directory
                destination_path = os.path.join(root_dir, filename)
                
                # Move the file to the root directory
                shutil.move(file_path, destination_path)
                print(f"Moved: {file_path} -> {destination_path}")

# Run the function
if __name__ == "__main__":
    move_jt_files()
