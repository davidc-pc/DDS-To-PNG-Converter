from wand.image import Image
from shutil import move
import os

def convert_dds_to_png(input_file, output_file):
    with Image(filename=input_file) as img:
        img.format = 'png'
        img.save(filename=output_file)

def move_to_old_files(input_file, old_files_folder):
    move(input_file, old_files_folder)

def main():
    input_folder = '.'  # Change this to the folder containing your .dds files
    output_folder = 'DDS Files (Game Ready)'  # Output folder for .png files
    old_files_folder = 'History'  # Folder for original .dds files
    os.makedirs(output_folder, exist_ok=True)

    try:
        for filename in os.listdir(input_folder):
            if filename.endswith(".png"):

                with Image(filename=filename) as img:
                    img.compression = "dxt3"
                    input_file = os.path.join(input_folder, filename)
                    output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.dds')
                    img.save(filename=output_file)
                    move_to_old_files(input_file, old_files_folder)
                    print(f"Converted {filename} to DDS")

        # Wait for user input before exiting
        input("Conversion completed. Press Enter to exit.")
    except Exception as e:
        with open("error_log.txt", "a") as f:
            f.write(f"Error converting files to DDS: {str(e)}\n")

if __name__ == "__main__":
    main()
