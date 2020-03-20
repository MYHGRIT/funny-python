# os.system("adb shell screencap -p /sdcard/screen.png") 
# os.system("adb pull /sdcard/screen.png")
#  255,155,174  x = 928  点击的位置
# //模拟滑动，从(250,250)滑动到(300,300)
# adb shell input swipe 250 250 300 300
# 567, 1754 567,245
from PIL import Image
import os
import time
        
# os.system("adb exec-out screencap -p > screen.png")
def get_Y_position():
    y_list = list()
    image = Image.open("screen.png")
    for x in [928]:
        for y in range(1920):
            if image.getpixel((x,y)) == (255,155,174,255):
                y_list.append(y)
    return y_list
# get_Y_position() 

def main():

    while True:
        # 截图
        os.system("adb exec-out screencap -p > screen.png")
        # 获得y的坐标吧
        y_list = get_Y_position()
        print(y_list)
        # 模拟点击
        for y in y_list:
            os.system("adb shell input tap 846 {}".format(y))
            time.sleep(0.5)
            print("正在关注")
        # 模拟翻页翻页 560
        os.system("adb shell input swipe 567 1700 567 900")
        time.sleep(1)

if __name__ == "__main__":
    main()