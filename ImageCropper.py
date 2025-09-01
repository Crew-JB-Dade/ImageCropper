from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

def crop_image(input_path, output_path, crop_size=(1300, 1552)):
    """
    이미지 파일을 불러와서 중앙 crop_size 영역만 잘라 저장합니다.
    """
    img = Image.open(input_path)
    w, h = img.size
    crop_w, crop_h = crop_size
    left = (w - crop_w) // 2
    top = (h - crop_h) // 2
    right = left + crop_w
    bottom = top + crop_h
    img_cropped = img.crop((left, top, right, bottom))
    img_cropped.save(output_path)
    print(f"이미지 잘라 저장 완료: {output_path}")

def batch_crop_images(input_files, output_folder, crop_size=(1300, 1552)):
    """
    여러 이미지 파일을 이름 변경 없이 지정 폴더에 저장
    :param input_files: 이미지 파일 경로 리스트
    :param output_folder: 저장할 폴더 경로
    :param crop_size: (width, height) 튜플
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for input_path in input_files:
        if os.path.exists(input_path):
            filename = os.path.basename(input_path)
            output_path = os.path.join(output_folder, filename)
            crop_image(input_path, output_path, crop_size)
        else:
            print(f"파일이 존재하지 않습니다: {input_path}")

if __name__ == "__main__":
    # 사용자에게 파일 선택 창을 띄워 이미지 파일 선택
    root = tk.Tk()
    root.withdraw()  # Tk 창 숨김
    input_files = filedialog.askopenfilenames(
        title="이미지 파일을 선택하세요",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    input_files = list(input_files)
    if not input_files:
        print("선택된 파일이 없습니다.")
    else:
        output_folder = "cropped_images"  # 저장할 폴더명
        batch_crop_images(input_files, output_folder)
