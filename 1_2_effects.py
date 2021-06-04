import cv2
import numpy as np # 行列計算ライブラリ、Numpyをインポート

key = 0

while True:
    img = cv2.imread("cat.jpg") # image read

    # 画像にエフェクトをかけていく
    if key is ord('a'): # Aが押された時
        img = cv2.blur(img,(15,31)) # 画像をぼかす（15, 35)はX,Y方向のぼかす大きさ

    elif key is ord('g'):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # グレースケールにする

    elif key is ord('e'):
        img = cv2.Canny(img,60,200) # 輪郭抽出

    elif key is ord('x'):
        # 油絵エフェクト
        # 第二引数はsize, 第三引数はdynRatio
        img = cv2.xphoto.oilPainting(img, 7, 2, cv2.COLOR_BGR2Lab)
    
    elif key is ord('h'):
        # 色空間の変換(RGB -> HSV)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    elif key is ord('b'):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # グレースケールにする
        ret3,img = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 大津の二値化

    
    # 上のようなエフェクト組み合わせて色々作っていくよ

    # 例1：グリーンバック
    elif key is ord('w'):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # 色空間の変換(RGB -> HSV)
        height, width, channel = img.shape
        print(hsv[10, 10])
        for x in range(width):
            for y in range(height):
                h, s, v= img[y, x]
                if 30 < h < 70 and s > 50: # 緑色の部分は
                    img[y, x]=[255, 0, 0] # 赤色にする
            
    # 例2：自力で輪郭抽出
    elif key is ord('v'):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # グレースケール化
        ret3,img_binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 二値化
        img_binary = cv2.bitwise_not(img_binary) # ネガポジ反転（findContours関数は白い部分を検出するため）
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 輪郭検出
        img = cv2.drawContours(img, contours, -1, (0, 255, 0), 5) # 輪郭描画


    cv2.imshow("test", img)
    key_tmp = cv2.waitKey(10)
    if key_tmp > 0: key = key_tmp

    if key == 27 or key == 113: break

