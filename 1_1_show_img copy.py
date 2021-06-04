# OpenCVライブラリを読み込む
import cv2

# 画像を読み込んでimg変数に格納
# print(img)をするとわかるが、imgはw * h * 3の大きさのnumpy行列
img = cv2.imread("cat.jpg")

while True:
    # testウィンドウにimgを表示
    cv2.imshow("test", img)

    # 10ms待つ。その間になにかキーボードが押されたらその数値を返してkeyに代入
    key = cv2.waitKey(10)
    # print(key)

    # ESCキーやQキーが押された場合は終了する
    if key == 27 or key == 113: break


