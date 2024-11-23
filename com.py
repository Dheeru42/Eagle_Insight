from plate import * 
from loc1 import *
import cv2
from PIL import Image
import pytesseract
from playsound import playsound

# Specify the Tesseract executable path if it's not in PATH (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to clean up the image
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Optionally, apply dilation/erosion to enhance text edges
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    processed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    return processed_image

def extract_text(image_path):

    # Perform OCR on the image
    text = pytesseract.image_to_string(Image.open(image_path), lang="eng", config="--oem 3 --psm 6")
    return text

# Input image path
image_path = r"D:\project\ml model\eagle\eagleinsight\static\images\1.png"  # Replace with your image file

while True:
    cap()
    text = extract_text(image_path)
    info = ''.join(e for e in text if e.isalnum())
    print("Number is:",info)
    
    ## <- testing 
    num = "RJ14CV0002"
    ## -> testing
    if text=="":
        while time.time() < end_time:
        # Play a warning sound file
            winsound.PlaySound("warning.wav", winsound.SND_FILENAME)
        
    if text==num:
        winsound.Beep(frequency, duration)
        while time.time() < end_time:
            beepy.beep(sound=1)
        send(text)
      
cv2.destroyAllWindows()




