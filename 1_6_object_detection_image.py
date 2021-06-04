import cv2
import numpy as np

img = cv2.imread('flower.jpg') # 画像読み込み

# HSV色空間に変換
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 画像をぼかす（15, 35)はX,Y方向のぼかす大きさ
# hsv_img = cv2.blur(hsv_img,(5,5)) 
# hsv_img = cv2.GaussianBlur(hsv_img, (9, 9), 3)

h_img = hsv_img[:, :, 0]
s_img = hsv_img[:, :, 1]
v_img = hsv_img[:, :, 2]

lower_th = (0, 100, 100)
higher_th = (10, 255, 255)

img_th = cv2.inRange(hsv_img, lower_th, higher_th)
# ret, img_th= cv2.threshold(h_img, 60, 255, cv2.THRESH_BINARY)
img_th = cv2.bitwise_not(img_th) # ネガポジ反転（findContours関数は白い部分を検出するため）


# 収縮・膨張処理
kernel = np.ones((3,3), np.uint8)
mask = cv2.dilate(img_th, kernel, iterations = 1) #縮小処理（ノイズ除去）
# mask = cv2.dilate(mask,  kernel, iterations = 1) # 拡大処理（凹んだ部分を埋める）

result = np.copy(img)

contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# labels, contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print("-------------------   Counters  -----------------------")
for c in contours:
    if cv2.contourArea(c) < 300: continue # オブジェクトが小さいときは無視する
    print(c)
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(result, (x, y), (x + w, y + h), (255, 255, 0), 2)
print("-------------------   Counters  -----------------------")


cv2.imshow("before", img)
cv2.imshow("result", result)
cv2.imshow("threshould", img_th)
cv2.imshow("mask", mask)

cv2.waitKey(0)
