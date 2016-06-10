#coding:utf-8
import urllib2,cookielib
import bs4

# url = "http://www.imooc.com/learn/615"
#
#
# print '第一种方法'
#
# response1 = urllib2.urlopen(url)
#
# print response1.getcode()
# print response1.read()
#
# print '第二种方法'
#
# request = urllib2.Request(url)
# request.add_header('user-agent','Mozilla/5.0')
#
# response2= urllib2.urlopen(request)
#
# print response2.getcode()
# print len(response2.read())
#
# print '第三种方法'
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#
# urllib2.install_opener(opener)
#
# response3 = urllib2.urlopen(url)
#
# print response3.getcode()
# print cj
# print len(response3.read())


# freader = urllib2.urlopen(self.__fileInfor.url[conf.STATE])
# filepath = self.filedir+os.sep+self.__fileInfor.filename+'.mp4'
# with open(filepath, "wb") as fwriter:
#     fwriter.write(freader.read())
#     fwriter.flush()
# fwriter.close()
import urllib
#下载文件
def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent
url = 'http://www.sina.com.cn'
local = 'd:\\sina.html'
urllib.urlretrieve(url, local, callbackfunc)
