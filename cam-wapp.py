#coding:utf-8
from VideoCapture import Device
import time
import win32gui,win32con,win32api
import Image

#初始化摄像头
cam = Device(devnum=0,showVideoWindow=0)
#抓图
cam.saveSnapshot('test.jpg',timestamp=3,boldfont=1,quality=75)
#休眠一秒
time.sleep(1)
img = Image.open('test.jpg')
if(img):
	img.save('test.bmp','BMP')
	# Update WallPaper
	print(u'正在设置图片:%s为桌面壁纸...' % 'test.bmp')
	key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
		"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
	win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
	win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
	win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, 'test.bmp', 1+2)
	print(u'成功应用图片:%s为桌面壁纸'  % 'test.bmp')


	
	



