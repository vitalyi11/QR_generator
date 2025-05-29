
import qrcode
from PIL import Image
import os

def generate_qr_code(url, filename="qrcode.png", box_size=10, border=4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {os.path.abspath(filename)}")
    return filename

def main():    
    url = input("URL: ")
    filename = input("Enter output filename: ")
    generate_qr_code(url, filename)
    print("QR code generated successfully!")

if __name__ == "__main__":
    main()