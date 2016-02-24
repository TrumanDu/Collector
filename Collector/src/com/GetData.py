#encoding:UTF-8
import re
import urllib.request
import Tool

class Spider:

    def __init__(self):
        self.siteURL = 'http://xa.ganji.com/zpdianhuaxiaoshou/o'
        self.tool = Tool.Tool()

    def getPage(self,pageIndex):
        url = self.siteURL + str(pageIndex)+"/"
        data=urllib.request.urlopen(url).read()
        z_data=data.decode('UTF-8')
        return z_data

    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<dl class="list-noimg job-list clearfix".*?<dd class="company">.*?<a href="(.*?)".*?</dd>',re.S)
        items = re.findall(pattern,page)
        for item in items:
#            print (item)
            self.getCompanyContents(item)
    def getCompanyContents(self,pageUrl):
            data=urllib.request.urlopen(pageUrl).read()
            z_data2=data.decode('UTF-8')
#            print (z_data)
            pattern2 = re.compile('<div class="c-age">(.*?)<img src="(.*?)".*?</div>',re.S)
            items = re.findall(pattern2,z_data2)
            for item in items:
#                print (self.tool.replace(item[0]),self.tool.replace(item[1]))
#                 print (self.tool.replace(item[0]))
                 self.saveImg(self.tool.replace(item[1]),self.tool.replaceCom(item[0]))
     #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL,fileName):
         url = '<img src="http://www.ganji.com' + imageURL+'"></li></ul>'
         f = open("companyInfo.html", 'a',encoding='utf-8')
         fileData = str(fileName)+url
         print ("正在悄悄保存企业机密信息")
         f.write(fileData)
         f.close()
        #传入起止页码
    def savePagesInfo(self,start,end):
        f = open("companyInfo.html", 'a',encoding='utf-8')
        f.write('<meta http-equiv="charset" content="utf-8">')
        f.close()
        for i in range(start,end+1):
            print ("正在偷偷寻找第"+str(i)+"页数据")
            self.getContents(i)
               
spider = Spider()
spider.savePagesInfo(1,10)
