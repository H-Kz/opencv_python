# http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_video_display/py_video_display.html
# https://www.pynote.info/entry/opencv-video-capture-and-writer

import numpy as np
import cv2


# 画像ファイルを読み込むやつ 
def open_image():
    # 画像を開く
    image_path = str(input_directory) + str(input_dname_common) + str(input_counter) + str(input_extention)
    # print(image_path + "\n")
    gif = cv2.VideoCapture(image_path)
    # 動画から1フレーム目を取り出す
    is_success, img = gif.read()
    # 画像が読み込まれなかったときに離脱
    if not is_success:
        out.release()
        cv2.destroyAllWindows()
        exit()
    
    '''
    よくわからんけど無くても動いた拡張子
    # gifからOpenCVに返すには配列にしないといけないらしい？
    # そのまま食わせると配列の形式とかの問題が起きた
    # https://start-python.hateblo.jp/entry/2019/12/30/090000
    # images = []
    # images.append(img)
    # img = images[0]
    '''

    return img

'''
ーーーーーー
読み込み設定
ーーーーーー
'''

# 読み込む画像のディレクトリを指定拡張子
input_directory = "/home/h-kz/shutokou/images/"
# 連番画像の共通部分
input_dname_common = "2020-02-20-"
# 連番画像の最初の番号を指定
input_counter = 213
# 連番画像の拡張子
input_extention = ".gif"
# 一枚の画像を何フレームの間表示するかを指定
frames = 3

# 入力画像を試しに読み込む
img = open_image()

# 入力画像の解像度を認識
# https://github.com/atinfinity/lab/wiki/%5BOpenCV-Python%5D%E7%94%BB%E5%83%8F%E3%81%AE%E5%B9%85%E3%80%81%E9%AB%98%E3%81%95%E3%80%81%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB%E6%95%B0%E3%80%81depth%E5%8F%96%E5%BE%97
# カラーとグレースケールで場合分け
if len(img.shape) == 3:
    height, width, channels = img.shape[:3]
else:
    height, width = img.shape[:2]
    channels = 1
# 取得結果（幅，高さ，チャンネル数，depth）を表示
print("input  file→   width: " + str(width)+"　　height: " + str(height)+"　　channels: " + str(channels)+"　　dtype: " + str(img.dtype))


'''
ーーーーーー
書き出し設定
ーーーーーー
'''
# 出力先のフォルダを指定
output_directry = "/home/h-kz/shutokou/gif/"
# 出力動画のファイル名を指定
output_name = "output"
output_path = str(output_directry) + str(output_name) + ".mp4"
print("output file→   "+ output_path + "\n")
# 出力動画のフレームレートを設定
output_fps = 30.0
# 出力動画の形式（ファイル名、エンコード、FPS,（幅、高さ））
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter(output_path,fourcc, output_fps, (width,height))


# 画像を表示するウインドウの形式
# cv2.namedWindow('test', cv2.WINDOW_NORMAL)

while True:
    img = open_image()

    tmp = 1
    while( tmp <= frames ):
        #１フレームずつ動画に追加する
        out.write(img)

        '''
        #観賞用に画像表示
        cv2.imshow('test', img)
        cv2.waitKey(20)
        # 書き込んだ画像の番号を表示
        print(str(input_counter) + ' '+ str(tmp)
        '''
        
        tmp += 1


    #テスト用の画像保存
    #cv2.imwrite('output'+str(input_counter)+'.jpg', img)
    input_counter += 1
    cv2.imwrite('output.jpg', img)
