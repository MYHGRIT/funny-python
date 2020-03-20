
from PIL import Image
import os
import time
import random
# 快手 双击取消广告点
# 470,1344 255,255,255
# 987 1358 点赞点
# 刷宝点赞点 996 867 
# 关注点 580 1475 X坐标不变,Y左边改变,所以待解决但是我没空改

class ShuaBao(object):
    # 分别是 每看多少个视频点一次赞,点赞坐标,每个视频的随机间隔5~15秒
    def __init__(self,like_interval = 3,like_coordinate=(996,867),watch_time = (2,5)):
        # 看了多少个视频
        self.vido_num = 0
        # 点了多少次赞
        self.like_num = 0
        # 点赞间隔
        self.like_interval = like_interval
        self.like_coordinate = like_coordinate
        self.watch_time = watch_time
    def give_like(self):
        if self.vido_num % self.like_interval == 0:
            # 模拟点赞
            os.system("adb shell input tap {} {}".format(self.like_coordinate[0],self.like_coordinate[1]))
            self.like_num+=1
            print("点了{}次赞".format(self.like_num))
    
    def watch_vido(self):
        croll_time = random.randint(*self.watch_time)
        time.sleep(croll_time)
        self.vido_num += 1
        print("看了{}个视频".format(self.vido_num))

    def run(self):
        while True:
            # 点赞
            self.give_like()
            # 看上一段时间
            self.watch_vido()
            # 向上滑动
            os.system("adb shell input swipe 567 1200 567 600")

class KuaiShou(ShuaBao):
    # 点赞坐标不同
    def __init__(self,AD_position = (471,1345),like_coordinate=(980,1353)):
        self.like_coordinate = like_coordinate
        # 快手和刷宝的关注点坐标不同
        super().__init__(like_coordinate=self.like_coordinate)
        self.click_ad_num = 0
        self.AD_position = AD_position

    def cancel_AD(self):
        # 截图
        os.system("adb exec-out screencap -p > screen.png")
        # 判断是否是广告
        image = Image.open("screen.png")
        if image.getpixel(self.AD_position) == (255,255,255,255):
            self.click_ad_num+=1
            print("取消了{}次广告".format(self.click_ad_num))
            # 如果是广告就双击一下
            os.system("adb shell input tap {} {}".format(self.AD_position[0],self.AD_position[1]))
            time.sleep(0.5)
            os.system("adb shell input tap {} {}".format(self.AD_position[0],self.AD_position[1]))

    def run(self):
        while True:
            self.cancel_AD()
            # 点赞
            self.give_like()
            # 看上一段时间
            self.watch_vido()
            # 向上滑动
            os.system("adb shell input swipe 567 1200 567 600")


# config_point = (472,1343)
def main():
    # shuabao = ShuaBao() # 这个是刷宝
    # shuabao.run() # 这个是刷宝
    kuaishou = KuaiShou() # 这个是快手
    kuaishou.run() # 这个是快手

if __name__ == "__main__":
    main()