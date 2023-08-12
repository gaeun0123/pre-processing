# 원하는 이미지 크롭 후, 라벨링 재설정 하는 코드
import cv2
import os

def crop_image_and_update_yolo_annotations(img_path, anno_path, output_folder, crop_box):
    img = cv2.imread(img_path)
    h, w, _ = img.shape
    x1, y1, x2, y2 = crop_box

    cropped_img = img[y1:y2, x1:x2]
    cropped_img_path = os.path.join(output_folder, os.path.basename(img_path))
    cv2.imwrite(cropped_img_path, cropped_img)

    # YOLO 형식 annotation 업로드
    with open(anno_path, 'r') as f:
        annotations = f.readlines()

    updated_annotations = []
    for line in annotations:
        parts = line.strip().split()
        class_id, x_center, y_center, width, height = map(float, parts)

        x_center_new = (x_center * w - x1) / (x2 - x1)
        y_center_new = (y_center * h - y1) / (y2 - y1)
        width_new = width * w / (x2 - x1)
        height_new = height * h / (y2 - y1)

        if 0 <= x_center_new <= 1 and 0 <= y_center_new <= 1:
            updated_annotations.append(f"{int(class_id)} {x_center_new} {y_center_new} {width_new} {height_new}\n")

    anno_output_path = os.path.join(output_folder, os.path.basename(anno_path))
    with open(anno_output_path, 'w') as f:
        f.writelines(updated_annotations)


# 본인 이미지 주소, annotation주소, 저장될 폴더 주소, crop할 영역 입력
if __name__ == '__main__':
    img_path = '/Users/choiga-eun/datasets/DenseHoneyBeeDetection_MultiClass.v9i.yolov8/test/Low_Quality/African-bees_jpg.rf.d5ec1d65aae05885cf806446e51e4909.jpg'
    anno_path = '/Users/choiga-eun/datasets/DenseHoneyBeeDetection_MultiClass.v9i.yolov8/test/low_label/African-bees_jpg.rf.d5ec1d65aae05885cf806446e51e4909.txt'
    output_folder = '/Users/choiga-eun/datasets/DenseHoneyBeeDetection_MultiClass.v9i.yolov8/test/low_images'
    # output폴더 경로를 못찾는 에러 -> 없으면 새로 폴더를 만드는 코드
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    #(x1, y1, x2, y2)
    crop_box = (100, 0, 800, 600)

    crop_image_and_update_yolo_annotations(img_path, anno_path, output_folder, crop_box)