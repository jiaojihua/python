import urllib.request as urllib2
import chardet
import gzip
response = urllib2.urlopen('http://www.baidu.com/')
html = response.read()
chardet.detect(html)
print(html)
