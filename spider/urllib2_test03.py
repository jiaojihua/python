import urllib
import urllib.request as urllib2


url = 'http://www.baidu.com/'

rawdata = urllib2.urlopen(url).read()
import chardet
chardet.detect(rawdata)

values = {'word':'hi'}
data = urllib.parse.urlencode(values).encode(encoding='UTF8')

req = urllib2.Request(url)
#添加http的header

req.add_header('User-Agent', 'Mozilla/5.0')

res = urllib2.urlopen(req)
the_page = res.read()
print (the_page)
