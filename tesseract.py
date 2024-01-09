import cv2
import pytesseract

# Set the Tesseract OCR executable path (replace with your actual path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jdg82\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)

title = ""  # OCR inference result string

while True:
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian filter to the grayscale frame
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    #edged = cv2.Canny(blurred_frame, 75, 200)

    cv2.imshow('title', blurred_frame)
    key = cv2.waitKey(1)  # pause the screen for a moment
    if key == ord('c'):
        # Perform OCR using pytesseract
        captured_text = pytesseract.image_to_string(blurred_frame, lang='kor')
        title = captured_text.strip()  # Remove leading/trailing whitespaces
        print("TITLE : ", title)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
