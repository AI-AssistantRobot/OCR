import cv2
import easyocr

reader = easyocr.Reader(['ko', 'en'], gpu=False)

cap = cv2.VideoCapture(0)

title = ""  #OCR 추론 결과 문자열

while True:
    ret, frame = cap.read()

    cv2.imshow('title', frame)
    key = cv2.waitKey(1) #화면 잠시 멈춤

    if key == ord('c'): #c 누르면 정지화면 -> c 대신 캡쳐 누르면 데이터 받을수 있게 진행
        captured_text = reader.readtext(frame, detail=0)
        title = "".join(captured_text) #문자열 저장
        print("TITLE : ", title)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
