# 해상도가 800, 600인 사진을 기준으로 낮으면 저화질 높으면 고화질로 나눈 후에
# 나눠진 대로 사진을 복사하여 폴더 생성

import os #폴더 만들기 
import cv2
import shutil #파일 복사를 위한 모듈

def classify_and_save_images_by_resolution(directory_path, threshold=(640, 640)):
 
    high_quality_dir = os.path.join(directory_path, 'High_Quality')
    low_quality_dir = os.path.join(directory_path, 'Low_Quality')

    # 폴더가 없으면 새로 생성
    if not os.path.exists(high_quality_dir):
        os.makedirs(high_quality_dir)
    if not os.path.exists(low_quality_dir):
        os.makedirs(low_quality_dir)

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(directory_path, filename)
            image = cv2.imread(image_path)

            if image is None:  # 이미지 파일이 아닌 경우 continue
                continue

            height, width = image.shape[:2]

            if width >= threshold[0] and height >= threshold[1]:
                shutil.copy(image_path, high_quality_dir)
            else:
                shutil.copy(image_path, low_quality_dir)

# 사용란
directory_path = '/'
classify_and_save_images_by_resolution(directory_path)

