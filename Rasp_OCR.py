import cv2
import requests
import numpy as np

# Flask 서버의 주소
server_address = 'http://192.168.1.186:5000/update_frame'

# 웹캠 초기화
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 'c' 키를 누르면 프레임을 서버에 전송
    if cv2.waitKey(1) & 0xFF == ord('c'):
        _, img_encoded = cv2.imencode('.jpg', frame)
        response = requests.post(server_address, files={'frame': ('frame.jpg', img_encoded.tobytes(), 'image/jpeg')})
        print(response.text)

    # 프레임 화면에 표시
    cv2.imshow('Frame', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 작업 완료 후 해제
cap.release()
cv2.destroyAllWindows()