#coding:utf-8
from VideoCapture import Device
import time

start = time.time()

#��ʼ������ͷ
cam = Device(devnum=0,showVideoWindow=0)

#ץͼ
cam.saveSnapshot('abc.jpg',timestamp=3,boldfont=1,quality=75)
end = time.time()

print(end-start)
