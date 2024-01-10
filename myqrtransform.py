import os
import qrcode
from PIL import Image

def generate_qr_code_with_icon(link, icon_path, output_path):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_img = qr.make_image( )

    # Open and resize the icon image
    icon = Image.open(icon_path)
    icon = icon.resize((50, 50))

    # Calculate the position to paste the icon in the center
    img_width, img_height = qr_img.size
    icon_width, icon_height = icon.size
    paste_position = ((img_width - icon_width) // 2, (img_height - icon_height) // 2)

    # Paste the icon onto the QR code
    qr_img.paste(icon, paste_position)

    # Save the final image
    qr_img.save(output_path)

if __name__ == "__main__":
    link = "https://www.linkedin.com/in/riad-bettole/"
    icon_filename = "174857.png"
    output_filename = "qrgit2.png"

    current_directory = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(current_directory, icon_filename)
    output_path = os.path.join(current_directory, output_filename)

    generate_qr_code_with_icon(link, icon_path, output_path)