import easyocr
import cv2

reader = easyocr.Reader(['ko', 'en'], gpu=False)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    text = reader.readtext(frame, detail=0)

    cv2.imshow('텍스트 인식', frame)
    print(text)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break