import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

    # Create the PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter

    # Store the page number for each section heading
    section_page_mapping = {}

    for section_name, img_path in images:
        if section_name not in section_page_mapping:
            # Record the page number for the section
            section_page_mapping[section_name] = c.getPageNumber() + 1
            
            # Add a blank page before the section heading
            #c.showPage()  # Blank page
            
            # Add section heading on the same page
            c.setFont("Helvetica", 36)
            c.drawString(72, height - 72, section_name)

            # Move to the next page for images
            c.showPage()  # New page for images

        img = Image.open(img_path)
        img_width, img_height = img.size

        # Define page margins
        left_margin = 72
        right_margin = 72
        top_margin = 72
        bottom_margin = 72

        # Calculate available width and height
        available_width = width - (left_margin + right_margin)
        available_height = height - (top_margin + bottom_margin)

        # Calculate aspect ratios
        img_aspect_ratio = img_height / img_width
        page_aspect_ratio = available_height / available_width

        if img_aspect_ratio > page_aspect_ratio:
            img_height = available_height
            img_width = img_height / img_aspect_ratio
        else:
            img_width = available_width
            img_height = img_width * img_aspect_ratio

        # Center the image on the page
        x_position = (width - img_width) / 2
        y_position = (height - img_height) / 2

        c.drawImage(img_path, x_position, y_position, width=img_width, height=img_height)
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

# Usage
folder_path = 'screenshots/AI2TS-2'  # Replace with your folder path
output_pdf = 'Tests/AI2TS-2.pdf'  # Output PDF file name
create_pdf_from_images(folder_path, output_pdf)
