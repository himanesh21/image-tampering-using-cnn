import os
import csv

# Replace 'your_root_directory' with the path of your root directory
root_directory = 'D:\others\project\CASIA\casia\Training'
csv_file_path = 'image_paths.csv'

# Create or overwrite the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the headers to the CSV file
    writer.writerow(['Image Absolute Path', 'Subfolder Name'])

    # Walk through the directory
    for subdir, dirs, files in os.walk(root_directory):
        for filename in files:
            # Check if the file is an image
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Write the absolute path and subfolder name to the CSV
                writer.writerow([os.path.join(subdir, filename), os.path.basename(subdir)])

print(f'CSV file created at {csv_file_path}')
