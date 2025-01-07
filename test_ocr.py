from PIL import Image
import pytesseract

# Ensure the correct Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Path to an example image
image_path = "C:\\Users\\Nitin\\Pictures\\Screenshots\\sample.png"

# Perform OCR on the image
text = pytesseract.image_to_string(Image.open(image_path))
print("Extracted Text:")
print(text)
