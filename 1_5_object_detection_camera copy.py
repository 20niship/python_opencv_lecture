import cv2
import numpy as np # 行列計算ライブラリ、Numpyをインポート

# VideoCapture オブジェクトを取得
cap = cv2.VideoCapture(0)

width = 10
height = 10
if cap.isOpened(): 
    # get vcap property 
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # float `width`
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float `height`
    # 以下の方法でも可
    # width  = cap.get(3)  # float `width`
    # height = cap.get(4)  # float `height`

    fps = cap.get(cv2.CAP_PROP_FPS)

    print("camera found!")
    print(f"width={width}, height={height}, fps={fps}")
else:
    print("カメラが取得できない！")
    import os
    os.exit()

# ここでは自分は映らない
# 背景画像を取得
ret, background = cap.read()
background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)  # グレースケールにする


#青色ブランク画像
blue_img = np.zeros((int(height), int(width), 3))
blue_img += [0,0,255][::-1] #RGBで青指定

while(True):
    ret, img = cap.read()

    #グレースケール化して、backgroundとの絶対値（背景差分）を求める
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # グレースケールにする
    diff_img = cv2.absdiff(background_gray, img_gray)

    #二値化処理(どちらか良さそうな方を使って)
    # img_th = cv2.threshold(diff_img, 10, 255,cv2.THRESH_BINARY)[1]
    ret3,img_th = cv2.threshold(diff_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 大津の二値化

    # 収縮・膨張処理
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.erode( img_th,kernel,iterations = 1) #縮小処理（ノイズ除去）
    mask = cv2.dilate(mask,kernel,iterations = 1) # 拡大処理（凹んだ部分を埋める）

    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # labels, contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        if cv2.contourArea(c) < 50: continue # オブジェクトが小さいときは無視する
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 10)

    cv2.imshow('camera',img_th)
    cv2.imshow('diff',diff_img)
    cv2.imshow('result', img)

    key = cv2.waitKey(1)
    if key == 27 or key == 113: break
