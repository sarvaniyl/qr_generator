import argparse
import os
import qrcode
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def generate_qr_code(url, output_dir, filename, fill_color="black", back_color="white"):
    """
    Generate a QR code with the given URL and save it as a PNG file.
    
    Args:
        url (str): URL to encode in the QR code
        output_dir (str): Directory to save the QR code
        filename (str): Filename for the QR code
        fill_color (str): Color of the QR code
        back_color (str): Background color of the QR code
    
    Returns:
        str: Path to the generated QR code
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.info(f"Created output directory: {output_dir}")
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the image
    output_path = os.path.join(output_dir, filename)
    img.save(output_path)
    logger.info(f"QR code generated successfully and saved to {output_path}")
    
    return output_path

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate a QR code for a URL')
    parser.add_argument('--url', type=str, help='URL to encode in the QR code')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get parameters from environment variables or use defaults
    url = args.url or os.environ.get('QR_DATA_URL', 'https://github.com/sarvaniyl')
    output_dir = os.environ.get('QR_CODE_DIR', 'qr_codes')
    filename = os.environ.get('QR_CODE_FILENAME', 'github_qr.png')
    fill_color = os.environ.get('FILL_COLOR', 'black')
    back_color = os.environ.get('BACK_COLOR', 'white')
    
    logger.info(f"Generating QR code for URL: {url}")
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"Filename: {filename}")
    logger.info(f"Fill color: {fill_color}")
    logger.info(f"Background color: {back_color}")
    
    # Generate QR code
    generate_qr_code(url, output_dir, filename, fill_color, back_color)

if __name__ == "__main__":
    main()
