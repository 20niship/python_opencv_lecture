import cv2
import numpy as np # 行列計算ライブラリ、Numpyをインポート

# VideoCapture オブジェクトを取得
cap = cv2.VideoCapture(0)
 
if cap.isOpened(): 
    # get vcap property 
    width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`
    # 以下の方法でも可
    # width  = cap.get(3)  # float `width`
    # height = cap.get(4)  # float `height`

    fps = cap.get(cv2.CAP_PROP_FPS)

    print("camera found!")
    print(f"width={width}, height={height}, fps={fps}")
else:
    print("カメラが取得できない！")

while(True):
    ret, img = cap.read()

    # ここにエフェクトを追加していく

    cv2.imshow('camera',img)

    key = cv2.waitKey(10)
    if key == 27 or key == 113: break
