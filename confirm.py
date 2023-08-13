# 이미지 경로가 맞는지 확인하는 코드
import cv2
import os

image_path = '/'

# 파일 경로 체크
if not os.path.exists(image_path):
    print(f"Image file does not exist: {image_path}")
else:
    # 이미지 로드
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Failed to load the image: {image_path}")
    else:
        # 이미지 표시 (확인용)
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
