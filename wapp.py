#coding:utf-8
import win32gui,win32con,win32api
import Image
import time

start = time.time()
img = Image.open('test.jpg')
img.save('test.bmp','BMP')
# Update WallPaper
print('��������ͼƬ:%sΪ�����ֽ...' % 'test.bmp')
key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
    "Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2������Ӧ����,0�������
win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, 'test.bmp', 1+2)
print('�ɹ�Ӧ��ͼƬ:%sΪ�����ֽ'  % 'test.bmp')
end = time.time()
print(end-start)