# 경계면에 있거나 나간 라벨을 삭제하여 어노테이션에 재반영하는 코드
import os

def filter_cropped_annotations(anno_path, output_folder):
    with open(anno_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        parts = line.strip().split()
        _, x_center, y_center, width, height = map(float, parts)

        if x_center - width/2 >= 0 and x_center + width/2 <= 1 and y_center - height/2 >= 0 and y_center + height/2 <= 1:
            new_lines.append(line)

    output_path = os.path.join(output_folder, os.path.basename(anno_path))
    with open(output_path, 'w') as f:
        f.writelines(new_lines)

def process_all_annotations(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            filter_cropped_annotations(file_path, output_folder)

if __name__ == '__main__':
    input_folder = '/'
    output_folder = '/'
    process_all_annotations(input_folder, output_folder)
