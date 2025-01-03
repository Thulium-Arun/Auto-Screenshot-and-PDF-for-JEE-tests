import os
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
import shutil


def create_pdf_from_images(folder_path, output_pdf):
    images = []
    index_sections = []

    # Collect images and sections from the folder
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.png'):
            section_name = filename.split("[")[1].split("]")[0]  # Extract section name without brackets
            images.append((section_name, os.path.join(folder_path, filename)))
            if section_name not in index_sections:
                index_sections.append(section_name)

    # Create the PDF in landscape mode (letter size in landscape)
    c = canvas.Canvas(output_pdf, pagesize=landscape(letter))
    width, height = landscape(letter)  # Now width=11 inches, height=8.5 inches

    # Store the page number for each section heading
    section_page_mapping = {}

    for section_name, img_path in images:
        if section_name not in section_page_mapping:
            # Record the page number for the section
            section_page_mapping[section_name] = c.getPageNumber() + 1
            
            # Add section heading on the same page
            c.setFont("Helvetica", 36)
            c.drawString(72, height - 72, section_name)

            # Move to the next page for images
            c.showPage()  # New page for images

        # Define page margins
        left_margin = 72
        right_margin = 72
        top_margin = 72
        bottom_margin = 72

        # Calculate available width and height
        available_width = width - (left_margin + right_margin)
        available_height = height - (top_margin + bottom_margin)

        # Scale the image to fit the page dimensions
        c.drawImage(img_path, left_margin, bottom_margin, width=available_width, height=available_height)
        c.showPage()  # Move to the next page for the next image

    # Add the index page with correct page numbers
    c.showPage()
    c.setFont("Helvetica", 36)
    c.drawString(72, height - 72, "Index")
    y_position = height - 120

    for section in index_sections:
        page_number = section_page_mapping[section]
        c.drawString(72, y_position, f"{section} - Page {page_number}")
        y_position -= 48  # Space between index entries

    # Save the PDF
    c.save()

def move_folder_to_used(source_dir, used_dir, folder_name):
    # Move the folder to the "used" directory
    source_folder = os.path.join(source_dir, folder_name)
    dest_folder = os.path.join(used_dir, folder_name)

    try:
        shutil.move(source_folder, dest_folder)
        print(f"Moved folder: {folder_name} to {dest_folder}")
    except Exception as e:
        print(f"Error moving folder {folder_name}: {e}")

def process_screenshots_folder(source_dir, used_dir):
    # Ensure the 'used' directory exists
    if not os.path.exists(used_dir):
        os.makedirs(used_dir)

    # Loop through all subfolders in the 'screenshots' directory
    for subfolder_name in os.listdir(source_dir):
        subfolder_path = os.path.join(source_dir, subfolder_name)

        # Only process if it's a subfolder (not a file)
        if os.path.isdir(subfolder_path):
            # Output PDF file name based on the subfolder name
            output_pdf = os.path.join('Tests', f"{subfolder_name}.pdf")

            # Call your existing function to create a PDF from images in the subfolder
            create_pdf_from_images(subfolder_path, output_pdf)

            # After processing, move the subfolder to the 'used' folder
            move_folder_to_used(source_dir, used_dir, subfolder_name)

# Define the source directory and the 'used' directory
source_directory = 'screenshots'  # Folder containing subfolders with screenshots
used_directory = 'Used'  # Folder where processed subfolders will be moved

# Call the function to process the screenshots folder
process_screenshots_folder(source_directory, used_directory)
