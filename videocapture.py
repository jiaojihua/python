#coding:utf-8
from VideoCapture import Device
import time

start = time.time()

#初始化摄像头
cam = Device(devnum=0,showVideoWindow=0)

#抓图
cam.saveSnapshot('abc.jpg',timestamp=3,boldfont=1,quality=75)
end = time.time()

print(end-start)
